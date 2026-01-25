import asyncio
import yaml
from pathlib import Path
from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http import models

from src.core.config.settings import settings
from src.core.providers.embeddings import EmbeddingFactory
from src.knowledge.loaders import DocumentLoader

REGISTRY_PATH = Path("corpus/registry.yaml")
RAW_DIR = Path("corpus/raw")
COLLECTION_NAME = "tfm_allucination_v1"

def load_registry():
    if not REGISTRY_PATH.exists():
        return {}
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def recreate_collection(client: QdrantClient, vector_size: int):
    """
    Recrea la colección con el tamaño de vector correcto.
    """
    if client.collection_exists(COLLECTION_NAME):
        print(f"Eliminando colección existente: {COLLECTION_NAME}")
        client.delete_collection(COLLECTION_NAME)
    
    print(f"Creando colección: {COLLECTION_NAME} (dim={vector_size})")
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE
        )
    )

def index_documents():
    # 1. Configurar Embeddings y Cliente
    print("Inicializando componentes...")
    embeddings = EmbeddingFactory.get_embeddings()
    
    # Probar embedding para obtener dimensión
    test_vec = embeddings.embed_query("test")
    vector_size = len(test_vec)
    print(f"Dimensión de embedding: {vector_size}")

    client = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
    recreate_collection(client, vector_size)

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
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
        # Intentar pdf y otras extensiones (o confiar en el registro, pero el glob simple es robusto)
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
            
            # Upsert (añadir documentos)
            if chunks:
                vector_store.add_documents(chunks)
                total_chunks += len(chunks)
                
        except Exception as e:
            print(f"ERROR indexando {doc_id}: {e}")

    print(f"\n¡Indexación Completada! Fragmentos totales: {total_chunks}")

if __name__ == "__main__":
    index_documents()
