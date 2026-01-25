import asyncio
import json
import os
import httpx
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Configuración
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OUTPUT_FILE = Path("src/core/config/model_registry.json")

# Lista estática para Gemini (ya que listar la API puede ser complejo o restringido)
GEMINI_MODELS = [
    {
        "id": "gemini-1.5-flash",
        "name": "Google Gemini 1.5 Flash",
        "provider": "gemini",
        "context_length": 1000000,
        "pricing": {"prompt": "0.0", "completion": "0.0"} # Placeholder o buscar precios reales
    },
    {
        "id": "gemini-1.5-pro",
        "name": "Google Gemini 1.5 Pro",
        "provider": "gemini",
        "context_length": 2000000,
        "pricing": {"prompt": "0.0", "completion": "0.0"}
    },
    {
        "id": "gemini-2.0-flash-exp",
        "name": "Google Gemini 2.0 Flash Experimental",
        "provider": "gemini",
        "context_length": 1000000,
        "pricing": {"prompt": "0.0", "completion": "0.0"}
    },
    {
        "id": "gemini-3-flash-preview",
        "name": "Google Gemini 3 Flash Preview",
        "provider": "gemini",
        "context_length": 1000000,
        "pricing": {"prompt": "0.0", "completion": "0.0"}
    }
]

async def fetch_openrouter_models():
    """Obtener modelos disponibles desde la API de OpenRouter."""
    url = "https://openrouter.ai/api/v1/models"
    headers = {}
    if OPENROUTER_API_KEY:
        headers["Authorization"] = f"Bearer {OPENROUTER_API_KEY}"
    
    print(f"Obteniendo modelos OpenRouter desde {url}...")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            models = []
            for item in data.get("data", []):
                # Extraer campos relevantes
                model_entry = {
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "provider": "openrouter",
                    "context_length": item.get("context_length"),
                    "pricing": item.get("pricing")
                }
                models.append(model_entry)
            
            print(f"Recuperados {len(models)} modelos de OpenRouter.")
            return models
        except Exception as e:
            print(f"Error obteniendo modelos OpenRouter: {e}")
            return []

async def main():
    # 1. Obtener modelos OpenRouter
    openrouter_models = await fetch_openrouter_models()
    
    # 2. Agrupar por proveedor
    # GEMINI_MODELS ya es una lista de dicts con "provider": "gemini"
    # openrouter_models es una lista de dicts con "provider": "openrouter"
    
    # 3. Crear estructura de registro
    registry = {
        "updated_at": os.popen("date /t").read().strip() if os.name == 'nt' else "now",
        "providers": {
            "gemini": GEMINI_MODELS,
            "openrouter": openrouter_models
        }
    }
    
    # 4. Guardar archivo
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
    
    print(f"Modelos guardados exitosamente en {OUTPUT_FILE}")
    print(f"  Gemini: {len(GEMINI_MODELS)}")
    print(f"  OpenRouter: {len(openrouter_models)}")

if __name__ == "__main__":
    asyncio.run(main())
