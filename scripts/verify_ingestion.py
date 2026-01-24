import argparse
import sys
import yaml
from pathlib import Path
from src.knowledge.loaders import DocumentLoader

REGISTRY_PATH = Path("corpus/registry.yaml")
RAW_DIR = Path("corpus/raw")

def load_registry():
    if not REGISTRY_PATH.exists():
        print(f"Registry not found at {REGISTRY_PATH}")
        return {}
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def verify_loaders():
    registry = load_registry()
    docs_metadata = registry.get("documents", [])
    
    print(f"Testing loaders on {len(docs_metadata)} documents from registry...")
    
    success_count = 0
    total_chunks = 0
    
    for doc_meta in docs_metadata:
        doc_id = doc_meta.get("id")
        file_path = RAW_DIR / f"{doc_id}.{doc_meta.get('type', 'pdf')}"
        
        # Handle some extension mismatches if type is generic
        if not file_path.exists():
            # Try finding file with that name independent of extension in yaml if mismatch
            candidates = list(RAW_DIR.glob(f"{doc_id}.*"))
            if candidates:
                file_path = candidates[0]
            else:
                print(f"[SKIP] File not found for {doc_id}")
                continue
                
        print(f"Loading {doc_id} ({file_path.name})...", end=" ")
        
        try:
            # Extract basic metadata to inject
            meta = {
                "title": doc_meta.get("title"),
                "country": doc_meta.get("country"),
                "year": doc_meta.get("year")
            }
            
            loaded_docs = DocumentLoader.load_document(file_path, doc_id=doc_id, extra_metadata=meta)
            
            if loaded_docs:
                print(f"OK. {len(loaded_docs)} chunks/pages.")
                success_count += 1
                total_chunks += len(loaded_docs)
                
                # Preview first doc content brevity
                # print(f"  Sample: {loaded_docs[0].page_content[:100]}...")
            else:
                print("EMPTY output.")
                
        except Exception as e:
            print(f"FAILED. Error: {e}")

    print(f"\nSummary: Successfully loaded {success_count}/{len(docs_metadata)} documents.")
    print(f"Total structured documents/pages created: {total_chunks}")

if __name__ == "__main__":
    verify_loaders()
