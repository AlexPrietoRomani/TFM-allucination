from langchain_google_genai import ChatGoogleGenerativeAI
from src.core.config.settings import settings

class GeminiProvider:
    @staticmethod
    def get_chat_model(model_name: str = "gemini-1.5-flash", **kwargs):
        """
        Retorna una instancia configurada de ChatGoogleGenerativeAI (Gemini).
        """
        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=settings.google_api_key,
            **kwargs
        )
