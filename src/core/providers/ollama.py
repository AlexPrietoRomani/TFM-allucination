from langchain_ollama import ChatOllama
from src.core.config.settings import settings

class OllamaProvider:
    @staticmethod
    def get_chat_model(model_name: str, **kwargs):
        """
        Returns a configured ChatOllama instance.
        """
        # Base URL can be configured in settings if needed, defaulting to standard local
        base_url = getattr(settings, "ollama_base_url", "http://localhost:11434")
        
        return ChatOllama(
            model=model_name,
            base_url=base_url,
            **kwargs
        )
