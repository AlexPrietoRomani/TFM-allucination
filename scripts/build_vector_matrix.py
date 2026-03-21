import os
import yaml
import time
import argparse
from pathlib import Path
from tqdm import tqdm
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_community.vectorstores import FAISS
from qdrant_client import QdrantClient
from qdrant_client.http import models

# Importar settings para configuraciones de base de datos
from src.core.config.settings import settings
from src.knowledge.loaders import DocumentLoader

# Directorios de interés
REGISTRY_PATH = Path("corpus/registry.yaml")
PARSED_DIR = Path("corpus/parsed")
OUTPUT_FAISS_DIR = Path("data/vector_matrix/faiss")
OUTPUT_QDRANT_DIR = Path("data/vector_matrix/qdrant_local")

# Definición de la Matriz de Experimentos
EMBEDDING_MODELS = ["mxbai-embed-large", "nomic-embed-text-v2-moe", "qwen3-embedding"]
CHUNK_STRATEGIES = [500, 1000, "semantic"]
DB_MOTORS = ["faiss", "qdrant_local"]  # Se puede expandir a qdrant_cloud si está configurado

MD_HEADERS_TO_SPLIT = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

def load_all_docs(limit: int = 0):
    """Carga documentos de corpus/parsed/ en memoria, con opción de límite."""
    if not PARSED_DIR.exists():
        print(f"❌ El directorio {PARSED_DIR} no existe.")
        return []

    print(f"Cargando archivos desde {PARSED_DIR}...")
    all_docs = []
    files = list(PARSED_DIR.glob("*.md"))
    if limit > 0:
        files = files[:limit]
        print(f"Limitiando carga a los primeros {limit} archivos...")

    for file_path in tqdm(files):
        try:
            doc_id = file_path.stem
            docs = DocumentLoader.load_parsed_md(file_path, doc_id=doc_id)
            if docs:
                all_docs.extend(docs)
        except Exception as e:
            print(f"ERROR cargando {file_path.name}: {e}")
    print(f"Total documentos base cargados: {len(all_docs)}")
    return all_docs

def get_chunks(all_docs, strategy):
    """Aplica el splitter correspondiente según la estrategia."""
    if strategy == 500:
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        return splitter.split_documents(all_docs)
    elif strategy == 1000:
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        return splitter.split_documents(all_docs)
    elif strategy == "semantic":
        # Divide por headers pero aplica un fallback para que no exceda límites de token
        md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=MD_HEADERS_TO_SPLIT, strip_headers=False)
        recursive_sub_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        
        all_chunks = []
        for doc in all_docs:
            try:
                header_chunks = md_splitter.split_text(doc.page_content)
                # Aplicar sub-splitter por caracteres para sub-dividir bloques gigantes
                final_sub_chunks = recursive_sub_splitter.split_documents(header_chunks)
                for chunk in final_sub_chunks:
                    # Conservar metadatos del documento original
                    chunk.metadata.update(doc.metadata)
                all_chunks.extend(final_sub_chunks)
            except Exception as e:
                 print(f"Error en split semántico para {doc.metadata.get('filename')}: {e}")
        return all_chunks
    else:
        raise ValueError(f"Estrategia de chunking '{strategy}' desconocida.")

def create_faiss_index(chunks, embeddings, output_path: Path):
    """Crea y persiste un índice FAISS local."""
    print(f"-> Creando FAISS en: {output_path}")
    start_time = time.time()
    try:
        db = FAISS.from_documents(chunks, embeddings)
        db.save_local(str(output_path))
    except Exception as e:
        print(f"  ⚠️ Error de indexación masiva ({e}). Filtrando fragmentos erróneos...")
        valid_chunks = []
        for chunk in tqdm(chunks, desc="Validando fragmentos"):
            try:
                embeddings.embed_query(chunk.page_content)
                valid_chunks.append(chunk)
            except Exception:
                continue
        if valid_chunks:
             print(f"  -> Indexando {len(valid_chunks)} fragmentos válidos restantes.")
             db = FAISS.from_documents(valid_chunks, embeddings)
             db.save_local(str(output_path))
        else:
             print("  ⚠️ No quedaron fragmentos válidos.")
    print(f"-> Guardado FAISS en {time.time() - start_time:.2f}s")

def create_qdrant_collection(chunks, embeddings, collection_name: str, client: QdrantClient):
    """Crea y puebla una colección en Qdrant."""
    print(f"-> Creando Qdrant: {collection_name}")
    start_time = time.time()
    
    # Obtener dimensiones
    test_vec = embeddings.embed_query("test")
    vector_size = len(test_vec)

    # Recrear colección para evitar datos sucios
    if client.collection_exists(collection_name):
        client.delete_collection(collection_name)

    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE
        )
    )

    batch_size = 50
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
        embedding=embeddings
    )
    
    # Inserción por lotes
    for i in tqdm(range(0, len(chunks), batch_size), desc=f"Indexando {collection_name}"):
        batch = chunks[i:i+batch_size]
        try:
            vector_store.add_documents(batch)
        except Exception as e:
            print(f"\n  ⚠️ Error en lote {i} ({e}). Procesando individualmente...")
            for chunk in batch:
                try:
                    # Validar si el embedding explota
                    embeddings.embed_query(chunk.page_content)
                    vector_store.add_documents([chunk])
                except Exception:
                    # Omitir fragmento que causa NaN u otros errores
                    continue
        
    print(f"-> Guardado Qdrant en {time.time() - start_time:.2f}s")

def main():
    parser = argparse.ArgumentParser(description="Construye la Matriz de Bases de Datos Vectoriales")
    parser.add_argument("--limit", type=int, default=0, help="Limitar número de documentos a procesar (para pruebas rápidas)")
    args = parser.parse_args()

    print("═══ CONSTRUCCIÓN DE LA MATRIZ DE EXPERIMENTOS VECTORIALES ═══")
    
    # Asegurar que existan los directorios
    OUTPUT_FAISS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_QDRANT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Carga masiva de documentos
    all_docs = load_all_docs(limit=args.limit)
    if not all_docs:
        print("No hay documentos que indexar.")
        return

    # Bucles de la Matriz
    for emb_model in EMBEDDING_MODELS:
        print(f"\n🔋 Iniciando con Embedding: [{emb_model.upper()}]")
        try:
            embeddings = OllamaEmbeddings(
                model=emb_model,
                base_url=settings.ollama_base_url
            )
            # Test de conectividad rápido antes de procesar chunks
            embeddings.embed_query("test_warmup")
        except Exception as e:
            print(f"❌ Error al calentar embedding {emb_model}. ¿Está descargado en Ollama? Saltando... ({e})")
            continue

        for chunk_strat in CHUNK_STRATEGIES:
            print(f"  ✂ Estrategia Chunking: [{str(chunk_strat).upper()}]")
            chunks = get_chunks(all_docs, chunk_strat)
            print(f"  -> {len(chunks)} fragmentos generados.")

            for db_motor in DB_MOTORS:
                # Formar ID de combinación
                comb_id = f"{emb_model.replace(':', '_')}_{chunk_strat}_{db_motor}"
                print(f"    🗄 DB Motor: [{db_motor.upper()}] -> ID: {comb_id}")

                try:
                    if db_motor == "faiss":
                        faiss_path = OUTPUT_FAISS_DIR / comb_id
                        create_faiss_index(chunks, embeddings, faiss_path)
                    elif db_motor == "qdrant_local":
                        qdrant_path = OUTPUT_QDRANT_DIR / comb_id
                        qclient = QdrantClient(path=str(qdrant_path))
                        collection_name = f"tfm_matrix_{comb_id.lower()}"
                        create_qdrant_collection(chunks, embeddings, collection_name, qclient)
                except Exception as e:
                    print(f"❌ Error en combinación {comb_id}: {e}")

    print("\n✅ Matriz de Base de Datos Vectoriales creada exitosamente.")

if __name__ == "__main__":
    main()
