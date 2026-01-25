import requests
from langchain_ollama import ChatOllama
from src.core.config.settings import settings

class OllamaProvider:
    @staticmethod
    def get_chat_model(model_name: str, **kwargs):
        """
        Retorna una instancia configurada de ChatOllama.
        """
        base_url = getattr(settings, "ollama_base_url", "http://localhost:11434")
        return ChatOllama(
            model=model_name,
            base_url=base_url,
            **kwargs
        )

    @staticmethod
    def unload_model(model_name: str):
        """
        Fuerza la descarga del modelo de la memoria estableciendo keep_alive a 0.
        Útil para ahorrar RAM en evaluaciones secuenciales.
        """
        base_url = getattr(settings, "ollama_base_url", "http://localhost:11434")
        try:
            print(f"Descargando modelo {model_name} de memoria...")
            # Enviamos una petición de generación vacía con keep_alive=0
            requests.post(
                f"{base_url}/api/generate",
                json={
                    "model": model_name,
                    "prompt": "",
                    "keep_alive": 0
                }
            )
            print(f"Modelo {model_name} descargado correctamente.")
        except Exception as e:
            print(f"Advertencia: Falló al descargar modelo Ollama: {e}")
