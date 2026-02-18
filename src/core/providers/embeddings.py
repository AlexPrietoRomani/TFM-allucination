"""
Fábrica de Embeddings — Siempre usa Ollama (nomic-embed-text).

El modelo nomic-embed-text (~274 MB) produce vectores de 768 dimensiones,
es 100% local, sin cuota de API, y tiene excelente calidad para RAG.

Si en un futuro se necesita Gemini embeddings, se puede habilitar 
cambiando DEFAULT_EMBEDDING_PROVIDER=gemini en .env
"""
from langchain_ollama import OllamaEmbeddings
from src.core.config.settings import settings


class EmbeddingFactory:
    """
    Fábrica de modelos de embeddings.
    Por defecto usa Ollama (nomic-embed-text) para operación 100% local.
    """

    @staticmethod
    def get_embeddings(provider: str = None):
        provider = provider or settings.default_embedding_provider

        if provider == "ollama":
            return OllamaEmbeddings(
                model="nomic-embed-text",
                base_url=settings.ollama_base_url,
            )
        elif provider == "gemini":
            from langchain_google_genai import GoogleGenerativeAIEmbeddings
            return GoogleGenerativeAIEmbeddings(
                model=settings.default_embedding_model,
                google_api_key=settings.google_api_key
            )
        else:
            raise ValueError(f"Proveedor de embeddings no soportado: {provider}")
