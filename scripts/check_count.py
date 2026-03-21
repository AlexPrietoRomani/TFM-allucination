#!/usr/bin/env python3
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.knowledge.indexer import get_qdrant_client, get_collection_name
from qdrant_client.http import models

def count_points():
    client = get_qdrant_client()
    collection_name = get_collection_name()
    try:
        count = client.count(
            collection_name=collection_name,
            exact=True
        )
        print(f"Colección: {collection_name}")
        print(f"Total puntos (chunks): {count.count}")
    except Exception as e:
        print(f"No se pudo contar puntos: {e}")

if __name__ == "__main__":
    count_points()
