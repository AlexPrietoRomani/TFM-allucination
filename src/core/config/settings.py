from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # API Keys
    google_api_key: str = Field(..., description="Google API Key for Gemini")
    openrouter_api_key: str = Field(..., description="OpenRouter API Key")

    # OpenRouter Config
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_http_referer: Optional[str] = None
    openrouter_x_title: Optional[str] = None

    # Defaults
    default_provider: str = "gemini"
    default_model_google: str = "gemini-3-flash-preview"
    default_model_openrouter: str = "openai/gpt-oss-120b:free"
    
    # Embeddings
    default_embedding_provider: str = "gemini" 
    default_embedding_model: str = "models/text-embedding-004"

    # Qdrant
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: Optional[str] = None

settings = AppSettings()
