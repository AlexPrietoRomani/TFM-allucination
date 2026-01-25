import argparse
import sys
import yaml
from pathlib import Path
from src.knowledge.loaders import DocumentLoader

REGISTRY_PATH = Path("corpus/registry.yaml")
RAW_DIR = Path("corpus/raw")

def load_registry():
    if not REGISTRY_PATH.exists():
        print(f"Registro no encontrado en {REGISTRY_PATH}")
        return {}
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def verify_loaders():
    registry = load_registry()
    docs_metadata = registry.get("documents", [])
    
    print(f"Probando cargadores en {len(docs_metadata)} documentos del registro...")
    
    success_count = 0
    total_chunks = 0
    
    for doc_meta in docs_metadata:
        doc_id = doc_meta.get("id")
        file_path = RAW_DIR / f"{doc_id}.{doc_meta.get('type', 'pdf')}"
        
        # Manejar discrepancias de extensión si el tipo es genérico
        if not file_path.exists():
            # Intentar encontrar archivo con ese nombre independiente de la extensión
            candidates = list(RAW_DIR.glob(f"{doc_id}.*"))
            if candidates:
                file_path = candidates[0]
            else:
                print(f"[RETIRO] Archivo no encontrado para {doc_id}")
                continue
                
        print(f"Cargando {doc_id} ({file_path.name})...", end=" ")
        
        try:
            # Extraer metadata básica para inyectar
            meta = {
                "title": doc_meta.get("title"),
                "country": doc_meta.get("country"),
                "year": doc_meta.get("year")
            }
            
            loaded_docs = DocumentLoader.load_document(file_path, doc_id=doc_id, extra_metadata=meta)
            
            if loaded_docs:
                print(f"OK. {len(loaded_docs)} fragmentos/páginas.")
                success_count += 1
                total_chunks += len(loaded_docs)
                
                # Vista previa del contenido (comentado)
                # print(f"  Muestra: {loaded_docs[0].page_content[:100]}...")
            else:
                print("Salida VACÍA.")
                
        except Exception as e:
            print(f"FALLÓ. Error: {e}")

    print(f"\nResumen: Cargados exitosamente {success_count}/{len(docs_metadata)} documentos.")
    print(f"Total de documentos/páginas estructurados creados: {total_chunks}")

if __name__ == "__main__":
    verify_loaders()
