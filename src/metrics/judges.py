from typing import Any
from src.core.providers.factory import ProviderFactory
from src.core.config.settings import settings

class JudgeFactory:
    @staticmethod
    def get_judge():
        """
        Retorna un LLM potente para actuar como juez.
        Por defecto usa Ollama gpt-oss:20b para ejecución local sin límites,
        pero podría cambiarse a GPT-4o o Gemini Pro en producción.
        """
        # Por defecto Ollama para ejecución local
        provider = "ollama"
        model = "gpt-oss:20b"
        
        return ProviderFactory.get_provider(provider, model)
