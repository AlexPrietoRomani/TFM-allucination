from src.core.providers.factory import ProviderFactory
from src.core.config.settings import settings


class JudgeFactory:
    @staticmethod
    def get_judge(provider: str = None, model: str = None):
        """
        Retorna un LLM para actuar como juez evaluador de métricas.
        """
        jud_provider = provider or "ollama"
        jud_model = model or settings.default_ollama_model
        
        return ProviderFactory.get_provider(jud_provider, jud_model)
