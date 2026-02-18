from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from src.core.config.settings import settings


class EmbeddingFactory:
    """
    Fábrica para obtener modelos de Embeddings.
    Soporta: Google Gemini (Text-Embedding-004) y Ollama (local).
    
    Ollama usa el modelo de embeddings 'nomic-embed-text' por defecto,
    que es ligero (~274 MB) y produce vectores de 768 dimensiones.
    """

    @staticmethod
    def get_embeddings(provider: str = None):
        provider = provider or settings.default_embedding_provider

        if provider == "gemini":
            if not settings.google_api_key:
                print("⚠ GOOGLE_API_KEY no configurada, usando Ollama embeddings como fallback")
                return EmbeddingFactory._get_ollama_embeddings()
            try:
                emb = GoogleGenerativeAIEmbeddings(
                    model=settings.default_embedding_model,
                    google_api_key=settings.google_api_key
                )
                # Test rápido para verificar que funciona
                emb.embed_query("test")
                return emb
            except Exception as e:
                print(f"⚠ Error con Gemini embeddings: {e}")
                print("  Usando Ollama embeddings como fallback...")
                return EmbeddingFactory._get_ollama_embeddings()

        elif provider == "ollama":
            return EmbeddingFactory._get_ollama_embeddings()

        else:
            raise ValueError(f"Proveedor de embeddings no soportado: {provider}")

    @staticmethod
    def _get_ollama_embeddings():
        """
        Retorna embeddings de Ollama usando nomic-embed-text.
        Este modelo produce vectores de 768 dimensiones y pesa ~274 MB.
        """
        return OllamaEmbeddings(
            model="nomic-embed-text",
            base_url=settings.ollama_base_url,
        )
