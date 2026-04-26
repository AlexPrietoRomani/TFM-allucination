import asyncio
import yaml
from pathlib import Path
from tqdm import tqdm
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter,
)
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http import models
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

from src.core.config.settings import settings
from src.core.providers.embeddings import EmbeddingFactory
from src.knowledge.loaders import DocumentLoader

REGISTRY_PATH = Path("corpus/registry.yaml")
RAW_DIR = Path("corpus/raw")
PARSED_DIR = Path("corpus/parsed")


def get_collection_name() -> str:
    """Retorna el nombre de la coleccion segun el provider de embeddings (para evitar colision de dimensiones)."""
    provider = settings.active_embedding_provider
    if provider == "gemini":
        return "tfm_allucination_gemini"
    return "tfm_allucination_ollama"


def get_qdrant_client() -> QdrantClient:
    """
    Retorna un QdrantClient configurado para el modo actual (local o cloud).
    """
    url = settings.active_qdrant_url
    api_key = settings.active_qdrant_api_key
    print(f"[Conectando] Qdrant ({settings.execution_mode}): {url}")
    return QdrantClient(url=url, api_key=api_key)


def load_registry():
    if not REGISTRY_PATH.exists():
        return {}
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def recreate_collection(client: QdrantClient, vector_size: int):
    """
    Recrea la coleccion con el tamano de vector correcto.
    """
    collection_name = get_collection_name()
    if client.collection_exists(collection_name):
        print(f"Eliminando coleccion existente: {collection_name}")
        client.delete_collection(collection_name)

    print(f"Creando coleccion: {collection_name} (dim={vector_size})")
    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE
        )
    )


@retry(
    wait=wait_exponential(multiplier=2, min=5, max=120),
    stop=stop_after_attempt(8),
    reraise=True,
)
def _embed_and_add(vector_store, chunks):
    """Envuelve la inserción con retries exponenciales para manejar Rate Limits."""
    vector_store.add_documents(chunks)


# En modo cloud, enviar chunks en lotes pequeños para no exceder RPM
BATCH_SIZE = 20  # 20 chunks por llamada → reduce presión sobre la API de embeddings


def _embed_and_add_batched(vector_store, chunks):
    """Inserta chunks en lotes, con retries por lote."""
    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        _embed_and_add(vector_store, batch)


# --- Splitters ---

# Para documentos pre-procesados (Markdown con headers de Docling)
MD_HEADERS_TO_SPLIT = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

# Para documentos raw (PyPDFLoader, DOCX, XLSX) — comportamiento original
RAW_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ". ", " ", ""]
)


def index_documents():
    # 1. Configurar Embeddings y Cliente
    print(f"=== Indexacion [{settings.execution_mode.upper()}] ===")
    print("Inicializando componentes...")
    embeddings = EmbeddingFactory.get_embeddings()

    # Probar embedding para obtener dimension
    test_vec = embeddings.embed_query("test")
    vector_size = len(test_vec)
    print(f"Dimension de embedding: {vector_size}")

    client = get_qdrant_client()
    recreate_collection(client, vector_size)

    collection_name = get_collection_name()
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
        embedding=embeddings
    )

    # 2. Cargar Documentos
    registry = load_registry()
    docs_metadata = registry.get("documents", [])

    # Splitter semántico para Markdown pre-procesado
    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=MD_HEADERS_TO_SPLIT,
        strip_headers=False,
    )

    total_chunks = 0
    parsed_count = 0
    raw_count = 0

    print(f"Indexando {len(docs_metadata)} documentos...")
    if PARSED_DIR.exists():
        print(f"[PARSED] Directorio parsed detectado: {PARSED_DIR}")

    for doc_meta in tqdm(docs_metadata):
        doc_id = doc_meta["id"]
        # Intentar pdf y otras extensiones
        candidates = list(RAW_DIR.glob(f"{doc_id}.*"))
        if not candidates:
            # Chequear si al menos existe un parsed
            parsed_path = PARSED_DIR / f"{doc_id}.md"
            if not parsed_path.exists():
                print(f"SALTAR: Archivo para {doc_id} no encontrado.")
                continue

        file_path = candidates[0] if candidates else None

        try:
            # Inyección de metadatos
            meta = {
                "title": doc_meta.get("title"),
                "country": doc_meta.get("country"),
                "year": doc_meta.get("year"),
                "source_id": doc_id
            }

            # Cargar (prioriza parsed si existe)
            raw_docs = DocumentLoader.load_document(
                file_path=file_path or Path("placeholder"),
                doc_id=doc_id,
                extra_metadata=meta,
                parsed_dir=PARSED_DIR
            )

            if not raw_docs:
                print(f"AVISO: Carga vacía para {doc_id}")
                continue

            # Elegir splitter según origen
            is_parsed = any(d.metadata.get("parsed") for d in raw_docs)

            if is_parsed:
                # MarkdownHeaderTextSplitter para docs pre-procesados
                all_chunks = []
                for doc in raw_docs:
                    md_chunks = md_splitter.split_text(doc.page_content)
                    # Propagar metadatos del documento original a cada chunk
                    for chunk in md_chunks:
                        chunk.metadata.update(doc.metadata)
                    all_chunks.extend(md_chunks)
                chunks = all_chunks
                parsed_count += 1
            else:
                # RecursiveCharacterTextSplitter para docs raw
                chunks = RAW_SPLITTER.split_documents(raw_docs)
                raw_count += 1

            print(f" -> {doc_id}: {len(chunks)} fragmentos ({'parsed' if is_parsed else 'raw'})")

            # Upsert con retries (protege contra Rate Limits en modo cloud)
            if chunks:
                _embed_and_add_batched(vector_store, chunks)
                total_chunks += len(chunks)

        except Exception as e:
            print(f"ERROR indexando {doc_id}: {e}")

    print(f"\nIndexacion Completada! Fragmentos totales: {total_chunks}")
    print(f"  -> Docs parsed (Docling):  {parsed_count}")
    print(f"  -> Docs raw (PyPDF/otros): {raw_count}")
    print(f"Coleccion: {collection_name}")

if __name__ == "__main__":
    index_documents()
