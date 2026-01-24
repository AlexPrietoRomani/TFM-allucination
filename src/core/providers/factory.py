import json
from pathlib import Path
from typing import Any, List, Dict
from src.core.providers.gemini import GeminiProvider
from src.core.providers.openrouter import OpenRouterProvider
from src.core.providers.ollama import OllamaProvider

REGISTRY_PATH = Path("src/core/config/model_registry.json")

class ProviderFactory:
    _models_cache: Dict[str, Any] = {}

    @classmethod
    def _load_registry(cls):
        """Loads model registry if not already loaded."""
        if cls._models_cache:
            return

        if REGISTRY_PATH.exists():
            try:
                with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    providers_data = data.get("providers", {})
                    for provider_key, models_list in providers_data.items():
                        for m in models_list:
                            cls._models_cache[m["id"]] = m
            except Exception as e:
                print(f"Warning: Failed to load model registry: {e}")
        else:
            print(f"Warning: Model registry not found at {REGISTRY_PATH}")

    @classmethod
    def validate_model(cls, model_name: str) -> bool:
        """Checks if model exists in registry. Returns True if found or registry missing."""
        cls._load_registry()
        if not cls._models_cache:
            return True
        
        if model_name not in cls._models_cache:
            # Log warning but allow proceeding (useful for custom/local models)
            # print(f"Warning: Model '{model_name}' not found in registry.")
            return False
        return True

    @staticmethod
    def get_provider(provider_name: str, model_name: str, **kwargs) -> Any:
        # Validate (just logs warning for now)
        ProviderFactory.validate_model(model_name)

        # Normalize provider name
        provider_name = provider_name.lower().strip()

        if provider_name == "gemini":
            return GeminiProvider.get_chat_model(model_name, **kwargs)
        elif provider_name == "openrouter":
            return OpenRouterProvider.get_chat_model(model_name, **kwargs)
        elif provider_name == "ollama":
            return OllamaProvider.get_chat_model(model_name, **kwargs)
        else:
            raise ValueError(f"Unknown provider: {provider_name}")
