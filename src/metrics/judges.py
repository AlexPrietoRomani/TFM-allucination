from typing import Any
from src.core.providers.factory import ProviderFactory
from src.core.config.settings import settings

class JudgeFactory:
    @staticmethod
    def get_judge():
        """
        Returns a strong LLM to act as a judge.
        Defaults to Gemini Flash/Pro or OpenRouter GPT-4o depending on settings.
        We prefer Gemini 1.5 Pro or Flash for speed/cost balance in this project.
        """
        # Default to Ollama as requested for local execution without rate limits
        provider = "ollama"
        model = "gpt-oss:20b"
        
        return ProviderFactory.get_provider(provider, model)
