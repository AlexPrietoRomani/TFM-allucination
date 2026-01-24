from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from src.core.config.settings import settings

class EmbeddingFactory:
    @staticmethod
    def get_embeddings(provider: str = None, model: str = None):
        provider = provider or settings.default_embedding_provider
        model = model or settings.default_embedding_model
        
        provider = provider.lower().strip()
        
        if provider == "gemini":
            return GoogleGenerativeAIEmbeddings(
                model=model,
                google_api_key=settings.google_api_key
            )
        elif provider == "openai" or provider == "openrouter":
            # Assuming OpenRouter compatible API or direct OpenAI
            # For OpenRouter embeddings, we often use the OpenAI SDK with base_url
            base_url = settings.openrouter_base_url if provider == "openrouter" else None
            api_key = settings.openrouter_api_key if provider == "openrouter" else None # Or separate key
            
            return OpenAIEmbeddings(
                model=model,
                openai_api_key=api_key,
                openai_api_base=base_url
            )
        else:
            raise ValueError(f"Unknown embedding provider: {provider}")
