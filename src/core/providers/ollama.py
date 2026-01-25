import requests
from langchain_ollama import ChatOllama
from src.core.config.settings import settings

class OllamaProvider:
    @staticmethod
    def get_chat_model(model_name: str, **kwargs):
        """
        Returns a configured ChatOllama instance.
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
        Forces the model to unload from memory by setting keep_alive to 0.
        """
        base_url = getattr(settings, "ollama_base_url", "http://localhost:11434")
        try:
            print(f"Unloading model {model_name} from memory...")
            # We send a generate request with empty prompt and keep_alive=0
            requests.post(
                f"{base_url}/api/generate",
                json={
                    "model": model_name,
                    "prompt": "",
                    "keep_alive": 0
                }
            )
            print(f"Model {model_name} unloaded successfully.")
        except Exception as e:
            print(f"Warning: Failed to unload Ollama model: {e}")
