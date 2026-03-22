#!/usr/bin/env python3
"""
test_vector_matrix_health.py — Diagnóstico de Salud para Matrices Vectoriales

Inspecciona los directorios `data/vector_matrix/faiss` y `data/vector_matrix/qdrant_local`,
verificando que existan los archivos de índice, que sean legibles y reportando 
la dimensión del vector y el número de elementos indexados (puntos).

Uso:
    uv run python tests/test_vector_matrix_health.py
"""

import sys
import os
from pathlib import Path

# Ajustar PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Imports directos para no depender de Ollama en las validaciones de carga
import faiss
from qdrant_client import QdrantClient

# Directorios
FAISS_DIR = PROJECT_ROOT / "data" / "vector_matrix" / "faiss"
QDRANT_DIR = PROJECT_ROOT / "data" / "vector_matrix" / "qdrant_local"

def format_size(size_in_bytes):
    """Formatea bytes a KB/MB de forma leíble."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} TB"

def check_faiss_health():
    print("\n📊 === DIAGNÓSTICO FAISS ===")
    if not FAISS_DIR.exists():
        print(f"Directory not found: {FAISS_DIR}")
        return

    subdirs = [d for d in FAISS_DIR.iterdir() if d.is_dir()]
    if not subdirs:
        print("No se encontraron índices FAISS.")
        return

    print(f"{'Combinación':<60} | {'Dim':<5} | {'Vectores':<10} | {'Peso'}")
    print("-" * 88)
    
    for subdir in subdirs:
         faiss_file = subdir / "index.faiss"
         pkl_file = subdir / "index.pkl"
         
         if faiss_file.exists() and pkl_file.exists():
              try:
                   # Leer índice directo con faiss (sin embeddings de Ollama)
                   index = faiss.read_index(str(faiss_file))
                   count = index.ntotal
                   dim = index.d
                   size = faiss_file.stat().st_size + pkl_file.stat().st_size
                   print(f"{subdir.name:<60} | {dim:<5} | {count:<10} | {format_size(size)}")
              except Exception as e:
                   print(f"{subdir.name:<60} | ERROR | No se pudo leer: {e}")
         else:
              print(f"{subdir.name:<60} | INCOMPLETO | Falta .faiss o .pkl")

def check_qdrant_health():
    print("\n📊 === DIAGNÓSTICO QDRANT LOCAL ===")
    if not QDRANT_DIR.exists():
        print(f"Directory not found: {QDRANT_DIR}")
        return

    subdirs = [d for d in QDRANT_DIR.iterdir() if d.is_dir()]
    if not subdirs:
        print("No se encontraron índices Qdrant Local.")
        return

    print(f"{'Combinación':<60} | {'Dim':<5} | {'Vectores':<10} | {'Colección'}")
    print("-" * 102)

    for subdir in subdirs:
         try:
              # QdrantClient(path=) lee base de datos SQLite/WAL de Qdrant-local
              client = QdrantClient(path=str(subdir))
              collections = client.get_collections().collections
              
              if collections:
                   coll_name = collections[0].name
                   coll_info = client.get_collection(collection_name=coll_name)
                   count = client.count(collection_name=coll_name).count
                   
                   # Obtener dimensión del primer punto o config
                   vector_config = coll_info.config.params.vectors
                   if hasattr(vector_config, 'size'):
                        dim = vector_config.size
                   else:
                        dim = "N/A" # En Qdrant con configuraciones múltiples no es directo
                        
                   print(f"{subdir.name:<60} | {dim:<5} | {count:<10} | {coll_name}")
              else:
                   print(f"{subdir.name:<60} | VACÍO | No hay colecciones")
         except Exception as e:
              print(f"{subdir.name:<60} | ERROR | No se pudo leer: {e}")

if __name__ == "__main__":
    print("═══ INSPECTOR DE BASES DE DATOS VECTORIALES ═══")
    check_faiss_health()
    check_qdrant_health()
    print("\n✅ Verificación finalizada.")
