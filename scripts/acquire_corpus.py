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
    # Deshabilitar verificación SSL para manejar algunos sitios institucionales con certificados antiguos
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
    
    # Verificar si existe y calcular checksum si es necesario (optimización: saltar si coincide)
    # Por ahora, forzamos descarga/verificación si checksum falta o archivo falta.
    
    if file_path.exists() and doc.get("checksum"):
        # Verificar existente
        current_checksum = calculate_checksum(file_path)
        if current_checksum == doc["checksum"]:
            return doc, "saltado (actualizado)"
    
    success, error = await download_file(url, file_path)
    if success:
        chk = calculate_checksum(file_path)
        doc["checksum"] = chk
        return doc, "descargado"
    else:
        print(f"Falló la descarga de {doc_id}: {error}")
        return doc, f"falló: {error}"

async def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    
    registry_data = load_registry()
    docs = registry_data.get("documents", [])
    
    print(f"Procesando {len(docs)} documentos...")
    
    updated_docs = []
    tasks = [process_document(doc) for doc in docs]
    
    results = await tqdm.gather(*tasks)
    
    for doc, status in results:
        print(f"[{doc['id']}] -> {status}")
        updated_docs.append(doc)
    
    # Actualizar registro con nuevos checksums
    registry_data["documents"] = updated_docs
    update_registry(registry_data)
    print("Registro actualizado.")

if __name__ == "__main__":
    asyncio.run(main())
