import asyncio
import json
import os
import httpx
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OUTPUT_FILE = Path("src/core/config/model_registry.json")

# Static list for Gemini (since API listing can be complex or restricted)
GEMINI_MODELS = [
    {
        "id": "gemini-1.5-flash",
        "name": "Google Gemini 1.5 Flash",
        "provider": "gemini",
        "context_length": 1000000,
        "pricing": {"prompt": "0.0", "completion": "0.0"} # Placeholder or look up real pricing
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
    """Fetch available models from OpenRouter API."""
    url = "https://openrouter.ai/api/v1/models"
    headers = {}
    if OPENROUTER_API_KEY:
        headers["Authorization"] = f"Bearer {OPENROUTER_API_KEY}"
    
    print(f"Fetching OpenRouter models from {url}...")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            models = []
            for item in data.get("data", []):
                # Extract relevant fields
                model_entry = {
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "provider": "openrouter",
                    "context_length": item.get("context_length"),
                    "pricing": item.get("pricing")
                }
                models.append(model_entry)
            
            print(f"Retrieved {len(models)} models from OpenRouter.")
            return models
        except Exception as e:
            print(f"Error fetching OpenRouter models: {e}")
            return []

async def main():
    # 1. Get OpenRouter models
    openrouter_models = await fetch_openrouter_models()
    
    # 2. Combine with Gemini models
    all_models = GEMINI_MODELS + openrouter_models
    
    # 3. Create registry structure
    registry = {
        "updated_at": os.popen("date /t").read().strip() if os.name == 'nt' else "now",
        "models": all_models
    }
    
    # 4. Save to file
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
    
    print(f"Successfully saved {len(all_models)} models to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
