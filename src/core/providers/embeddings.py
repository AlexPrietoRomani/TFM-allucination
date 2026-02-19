from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from src.core.config.settings import settings

class EmbeddingFactory:
    
    @staticmethod
    def get_embeddings(provider: str = None):
        """
        Retorna la instancia de Embeddings configurada.
        Por defecto usa 'settings.default_embedding_provider' (ollama).
        """
        provider = provider or settings.default_embedding_provider
        
        if provider == "gemini":
            if not settings.google_api_key:
                print("⚠ GOOGLE_API_KEY no configurada. Usando Ollama (fallback).")
                return EmbeddingFactory._get_ollama_embeddings()
            try:
                # Test rápido
                emb = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=settings.google_api_key)
                emb.embed_query("test") 
                return emb
            except Exception as e:
                print(f"⚠ Fallo con Gemini embeddings: {e}")
                print("  Usando Ollama (fallback)...")
                return EmbeddingFactory._get_ollama_embeddings()
        
        elif provider == "ollama":
            return EmbeddingFactory._get_ollama_embeddings()
            
        else:
            raise ValueError(f"Proveedor de embeddings no soportado: {provider}")

    @staticmethod
    def _get_ollama_embeddings():
        """
        Retorna embeddings locales con Ollama.
        Modelo configurado en settings.default_embedding_model (ej: mxbai-embed-large).
        """
        model_name = settings.default_embedding_model
        print(f"Combinando con Ollama Embeddings: {model_name}...")
        return OllamaEmbeddings(
            model=model_name,
            base_url=settings.ollama_base_url,
        )
