from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # API Keys (Optional: empty if only Ollama is used)
    google_api_key: str = Field(default="", description="Google API Key for Gemini")
    openrouter_api_key: str = Field(default="", description="OpenRouter API Key")

    # Default Models
    default_provider: str = "gemini"
    # Fallback models if API keys are missing
    default_model_google: str = "gemini-1.5-flash" 
    default_model_openrouter: str = "openai/gpt-4o-mini"
    
    # Ollama Default LLM (Local)
    default_ollama_model: str = "qwen2.5:3b"
    
    # Embeddings Configuration
    # Options: "gemini" (cloud), "ollama" (local)
    default_embedding_provider: str = "ollama" 
    
    # Ollama Embedding Model
    # Recomendado: "mxbai-embed-large" (SOTA, 670MB) o "nomic-embed-text" (Liagero, 274MB)
    default_embedding_model: str = "mxbai-embed-large"

    # Qdrant Configuration (Vector Database)
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: Optional[str] = None
    
    # Ollama Configuration (Local)
    ollama_base_url: str = "http://localhost:11434"

settings = Settings()
