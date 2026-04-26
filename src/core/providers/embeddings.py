from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from src.core.config.settings import settings

class EmbeddingFactory:

    @staticmethod
    def get_embeddings(provider: str = None):
        """
        Retorna la instancia de Embeddings configurada.
        
        Si no se especifica proveedor, se usa `settings.active_embedding_provider`,
        que depende del EXECUTION_MODE:
          - local  → Ollama (mxbai-embed-large)
          - cloud  → Gemini (text-embedding-004)
        """
        provider = provider or settings.active_embedding_provider

        if provider == "gemini":
            return EmbeddingFactory._get_gemini_embeddings()
        elif provider == "ollama":
            return EmbeddingFactory._get_ollama_embeddings()
        else:
            raise ValueError(f"Proveedor de embeddings no soportado: {provider}")

    @staticmethod
    def _get_gemini_embeddings():
        """
        Retorna embeddings en la nube con Google Gemini.
        Modelo: gemini-embedding-001 (3072d).
        """
        if not settings.google_api_key:
            if settings.is_cloud:
                raise ValueError(
                    "EXECUTION_MODE=cloud pero GOOGLE_API_KEY no está configurada. "
                    "Configúrala en .env o cambia a EXECUTION_MODE=local."
                )
            print("[AVISO] GOOGLE_API_KEY no configurada. Usando Ollama (fallback).")
            return EmbeddingFactory._get_ollama_embeddings()
        try:
            model = getattr(settings, "default_embedding_model_cloud", "models/gemini-embedding-001")
            
            # Si el usuario no pasó el prefijo 'models/'
            if not model.startswith("models/"):
                model = f"models/{model}"
                
            emb = GoogleGenerativeAIEmbeddings(
                model=model,
                google_api_key=settings.google_api_key
            )
            # Test rápido de conectividad
            emb.embed_query("test")
            print(f"[CLOUD] Embeddings: Google Gemini ({model})")
            return emb
        except Exception as e:
            if settings.is_cloud:
                raise RuntimeError(
                    f"Error conectando a Gemini Embeddings en modo cloud: {e}"
                ) from e
            print(f"[AVISO] Fallo con Gemini embeddings: {e}")
            print("  Usando Ollama (fallback)...")
            return EmbeddingFactory._get_ollama_embeddings()

    @staticmethod
    def _get_ollama_embeddings():
        """
        Retorna embeddings locales con Ollama.
        Modelo configurado en settings.default_embedding_model (ej: mxbai-embed-large).
        """
        if hasattr(settings, "default_embedding_model_local"):
            model = settings.default_embedding_model_local
        else: # Retrocompatibilidad
            model = getattr(settings, "default_embedding_model", "mxbai-embed-large")
        
        print(f"[LOCAL] Embeddings: Ollama local ({model})")
            
        return OllamaEmbeddings(
            model=model,
            base_url=settings.ollama_base_url,
        )
