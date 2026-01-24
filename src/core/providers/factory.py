from typing import Any
from src.core.providers.gemini import GeminiProvider
from src.core.providers.openrouter import OpenRouterProvider

class ProviderFactory:
    @staticmethod
    def get_provider(provider_name: str, model_name: str, **kwargs) -> Any:
        # Normalize provider name
        provider_name = provider_name.lower().strip()

        if provider_name == "gemini":
            return GeminiProvider.get_chat_model(model_name, **kwargs)
        elif provider_name == "openrouter":
            return OpenRouterProvider.get_chat_model(model_name, **kwargs)
        else:
            raise ValueError(f"Unknown provider: {provider_name}")
