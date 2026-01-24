from langchain_google_genai import ChatGoogleGenerativeAI
from src.core.config.settings import settings

class GeminiProvider:
    @staticmethod
    def get_chat_model(model_name: str = "gemini-1.5-flash", **kwargs):
        """
        Returns a configured ChatGoogleGenerativeAI instance.
        """
        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=settings.google_api_key,
            **kwargs
        )
