from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from src.core.config.settings import settings

class EmbeddingFactory:
    """
    Fábrica para obtener modelos de Embeddings.
    Actualmente estandarizado en Google Gemini (Text-Embedding-004) para consistencia vectorial.
    """
    @staticmethod
    def get_embeddings():
        # Por ahora hardcodemmos Google, pero listo para soportar OpenAI/HuggingFace
        if settings.default_embedding_provider == "gemini":
            return GoogleGenerativeAIEmbeddings(
                model=settings.default_embedding_model,
                google_api_key=settings.google_api_key
            )
        else:
            raise ValueError("Solo 'gemini' está soportado para embeddings actualmente.")
