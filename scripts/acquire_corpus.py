import yaml
import httpx
import hashlib
import asyncio
from pathlib import Path
from tqdm.asyncio import tqdm

REGISTRY_PATH = Path("corpus/registry.yaml")
RAW_DIR = Path("corpus/raw")

def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def update_registry(data):
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

def calculate_checksum(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

async def download_file(url, valid_path):
    # Disable SSL verification to handle some institutional sites with legacy certs
    async with httpx.AsyncClient(follow_redirects=True, timeout=60.0, verify=False) as client:
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            with open(valid_path, "wb") as f:
                f.write(resp.content)
            return True, None
        except Exception as e:
            return False, str(e)

async def process_document(doc):
    doc_id = doc["id"]
    url = doc["url"]
    file_path = RAW_DIR / f"{doc_id}.pdf"
    
    # Check if exists and calculate checksum if needed (optimization: skip if checksum matches)
    # For now, we force download/verify if checksum missing or file missing.
    
    if file_path.exists() and doc.get("checksum"):
        # Verify existing
        current_checksum = calculate_checksum(file_path)
        if current_checksum == doc["checksum"]:
            return doc, "skipped (up to date)"
    
    success, error = await download_file(url, file_path)
    if success:
        chk = calculate_checksum(file_path)
        doc["checksum"] = chk
        return doc, "downloaded"
    else:
        print(f"Failed to download {doc_id}: {error}")
        return doc, f"failed: {error}"

async def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    
    registry_data = load_registry()
    docs = registry_data.get("documents", [])
    
    print(f"Processing {len(docs)} documents...")
    
    updated_docs = []
    tasks = [process_document(doc) for doc in docs]
    
    results = await tqdm.gather(*tasks)
    
    for doc, status in results:
        print(f"[{doc['id']}] -> {status}")
        updated_docs.append(doc)
    
    # Update registry with new checksums
    registry_data["documents"] = updated_docs
    update_registry(registry_data)
    print("Registry updated.")

if __name__ == "__main__":
    asyncio.run(main())
