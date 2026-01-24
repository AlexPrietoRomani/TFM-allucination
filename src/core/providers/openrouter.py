from langchain_openai import ChatOpenAI
from src.core.config.settings import settings

class OpenRouterProvider:
    @staticmethod
    def get_chat_model(model_name: str, **kwargs):
        """
        Returns a configured ChatOpenAI instance pointing to OpenRouter.
        """
        extra_headers = {}
        if settings.openrouter_http_referer:
            extra_headers["HTTP-Referer"] = settings.openrouter_http_referer
        if settings.openrouter_x_title:
            extra_headers["X-Title"] = settings.openrouter_x_title

        return ChatOpenAI(
            base_url=settings.openrouter_base_url,
            api_key=settings.openrouter_api_key,
            model=model_name,
            default_headers=extra_headers,
            **kwargs
        )
