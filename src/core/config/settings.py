from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

class AppSettings(BaseSettings):
    """
    Configuración principal de la aplicación usando Pydantic.
    Carga variables desde el archivo .env.
    """
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Claves de API (Opcionales: vacías si solo se usa Ollama)
    google_api_key: str = Field(default="", description="API Key de Google para Gemini")
    openrouter_api_key: str = Field(default="", description="API Key de OpenRouter")

    # Configuración de OpenRouter
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_http_referer: Optional[str] = None
    openrouter_x_title: Optional[str] = None

    # Modelos por Defecto
    default_provider: str = "gemini"
    default_model_google: str = "gemini-3-flash-preview"
    default_model_openrouter: str = "openai/gpt-oss-120b:free"
    default_ollama_model: str = "qwen2.5:3b"
    
    # Configuración de Embeddings
    default_embedding_provider: str = "gemini" 
    default_embedding_model: str = "models/text-embedding-004"

    # Configuración de Qdrant (Base Vectorial)
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: Optional[str] = None
    
    # Configuración Ollama (Local)
    ollama_base_url: str = "http://localhost:11434"

settings = AppSettings()
