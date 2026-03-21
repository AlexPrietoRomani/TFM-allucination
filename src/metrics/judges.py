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
        
        # Si el usuario pide ollama explícitamente, forzar local para que el modo Cloud
        # no lo redirigiera a Gemini, manteniendo la independencia del evaluador.
        force_local = (jud_provider == "ollama")
        
        # Forzar formato JSON para Ollama en tareas de dictaminación de métricas
        kwargs = {}
        if jud_provider == "ollama":
            kwargs["format"] = "json"
            
        return ProviderFactory.get_provider(jud_provider, jud_model, force_local=force_local, **kwargs)
