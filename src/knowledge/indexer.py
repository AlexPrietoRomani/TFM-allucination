import asyncio
import yaml
from pathlib import Path
from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http import models
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

from src.core.config.settings import settings
from src.core.providers.embeddings import EmbeddingFactory
from src.knowledge.loaders import DocumentLoader

REGISTRY_PATH = Path("corpus/registry.yaml")
RAW_DIR = Path("corpus/raw")


def get_collection_name() -> str:
    """Retorna el nombre de la colección según el provider de embeddings (para evitar colisión de dimensiones)."""
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
    print(f"🔗 Conectando a Qdrant ({settings.execution_mode}): {url}")
    return QdrantClient(url=url, api_key=api_key)


def load_registry():
    if not REGISTRY_PATH.exists():
        return {}
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def recreate_collection(client: QdrantClient, vector_size: int):
    """
    Recrea la colección con el tamaño de vector correcto.
    """
    collection_name = get_collection_name()
    if client.collection_exists(collection_name):
        print(f"Eliminando colección existente: {collection_name}")
        client.delete_collection(collection_name)

    print(f"Creando colección: {collection_name} (dim={vector_size})")
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


def index_documents():
    # 1. Configurar Embeddings y Cliente
    print(f"═══ Indexación [{settings.execution_mode.upper()}] ═══")
    print("Inicializando componentes...")
    embeddings = EmbeddingFactory.get_embeddings()

    # Probar embedding para obtener dimensión
    test_vec = embeddings.embed_query("test")
    vector_size = len(test_vec)
    print(f"Dimensión de embedding: {vector_size}")

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

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    total_chunks = 0

    print(f"Indexando {len(docs_metadata)} documentos...")

    for doc_meta in tqdm(docs_metadata):
        doc_id = doc_meta["id"]
        # Intentar pdf y otras extensiones
        candidates = list(RAW_DIR.glob(f"{doc_id}.*"))
        if not candidates:
            print(f"SALTAR: Archivo para {doc_id} no encontrado.")
            continue

        file_path = candidates[0]

        try:
            # Inyección de metadatos
            meta = {
                "title": doc_meta.get("title"),
                "country": doc_meta.get("country"),
                "year": doc_meta.get("year"),
                "source_id": doc_id
            }

            # Cargar
            raw_docs = DocumentLoader.load_document(file_path, doc_id=doc_id, extra_metadata=meta)

            if not raw_docs:
                print(f"AVISO: Carga vacía para {doc_id}")
                continue

            # Dividir / Split
            chunks = splitter.split_documents(raw_docs)
            print(f" -> {doc_id}: {len(chunks)} fragmentos")

            # Upsert con retries (protege contra Rate Limits en modo cloud)
            if chunks:
                _embed_and_add_batched(vector_store, chunks)
                total_chunks += len(chunks)

        except Exception as e:
            print(f"ERROR indexando {doc_id}: {e}")

    print(f"\n¡Indexación Completada! Fragmentos totales: {total_chunks}")
    print(f"Colección: {collection_name}")

if __name__ == "__main__":
    index_documents()
