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
    Recreates the collection with the correct vector size.
    """
    if client.collection_exists(COLLECTION_NAME):
        print(f"Deleting existing collection: {COLLECTION_NAME}")
        client.delete_collection(COLLECTION_NAME)
    
    print(f"Creating collection: {COLLECTION_NAME} (dim={vector_size})")
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE
        )
    )

def index_documents():
    # 1. Setup Embeddings & Client
    print("Initializing components...")
    embeddings = EmbeddingFactory.get_embeddings()
    
    # Test embedding to get dimension
    test_vec = embeddings.embed_query("test")
    vector_size = len(test_vec)
    print(f"Embedding dimension: {vector_size}")

    client = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
    recreate_collection(client, vector_size)

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings
    )

    # 2. Load Documents
    registry = load_registry()
    docs_metadata = registry.get("documents", [])
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    total_chunks = 0
    
    print(f"Indexing {len(docs_metadata)} documents...")
    
    for doc_meta in tqdm(docs_metadata):
        doc_id = doc_meta["id"]
        # Try both pdf and other extensions (or trust registry, but some mismatches happened)
        # Using simple glob is robust.
        candidates = list(RAW_DIR.glob(f"{doc_id}.*"))
        if not candidates:
            print(f"SKIP: File for {doc_id} not found.")
            continue
        
        file_path = candidates[0]
        
        try:
            # Metadata injection
            meta = {
                "title": doc_meta.get("title"),
                "country": doc_meta.get("country"),
                "year": doc_meta.get("year"),
                "source_id": doc_id
            }
            
            # Load
            raw_docs = DocumentLoader.load_document(file_path, doc_id=doc_id, extra_metadata=meta)
            
            if not raw_docs:
                print(f"WARN: Empty load for {doc_id}")
                continue

            # Split
            chunks = splitter.split_documents(raw_docs)
            print(f" -> {doc_id}: {len(chunks)} chunks")
            
            # Upsert (in batches handled by vector_store usually, but we call add_documents)
            if chunks:
                vector_store.add_documents(chunks)
                total_chunks += len(chunks)
                
        except Exception as e:
            print(f"ERROR indexing {doc_id}: {e}")

    print(f"\nIndexing Complete! Total chunks: {total_chunks}")

if __name__ == "__main__":
    index_documents()
