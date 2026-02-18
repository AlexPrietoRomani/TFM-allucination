from src.core.providers.factory import ProviderFactory
from src.core.config.settings import settings


class JudgeFactory:
    @staticmethod
    def get_judge():
        """
        Retorna un LLM para actuar como juez evaluador de métricas.
        
        Usa Ollama local por defecto para:
          - Sin límites de API / cuota
          - Evaluación reproducible
          - Costo cero
        
        El modelo se puede cambiar con DEFAULT_OLLAMA_MODEL en .env
        """
        provider = "ollama"
        model = settings.default_ollama_model  # qwen2.5:3b por defecto
        
        return ProviderFactory.get_provider(provider, model)
