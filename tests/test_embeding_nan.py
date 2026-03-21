import os
import argparse
from tqdm import tqdm
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Forzar PYTHONPATH=.
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.core.config.settings import settings
from scripts.build_vector_matrix import load_all_docs

def main():
    print("Iniciando prueba de BGE-M3 con Chunk 500...")
    all_docs = load_all_docs(limit=1)
    if not all_docs:
        print("No hay documentos.")
        return

    # Splitter 500
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(all_docs)
    print(f"Total fragmentos divididos: {len(chunks)}")

    embeddings = OllamaEmbeddings(
        model="bge-m3",
        base_url=settings.ollama_base_url
    )

    print("Comenzando embeddings fragmento a fragmento...")
    success_count = 0
    fail_count = 0

    with open("failed_chunks.txt", "w", encoding="utf-8") as f_out:
        for i, chunk in enumerate(tqdm(chunks)):
            try:
                embeddings.embed_query(chunk.page_content)
                success_count += 1
            except Exception as e:
                fail_count += 1
                f_out.write(f"=== ERROR FRAGMENTO {i} ===\n")
                f_out.write(f"Mensaje: {e}\n")
                f_out.write(f"Contenido:\n{chunk.page_content}\n")
                f_out.write("============================\n\n")

    print(f"\nProceso terminado. Éxitos: {success_count}, Fallos: {fail_count}")

if __name__ == "__main__":
    main()
