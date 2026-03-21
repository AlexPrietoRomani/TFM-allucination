from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field
from typing import Optional, Literal

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # ── Execution Mode ───────────────────────────────────────────────────
    execution_mode: Literal["local", "cloud"] = Field(
        default="local",
        description="Execution mode: 'local' (Qdrant + Ollama) or 'cloud' (Qdrant Cloud + Gemini/OpenRouter)"
    )

    # ── API Keys (Optional: empty if only Ollama is used) ────────────────
    google_api_key: str = Field(default="", description="Google API Key for Gemini")
    openrouter_api_key: str = Field(default="", description="OpenRouter API Key")

    # ── OpenRouter ───────────────────────────────────────────────────────
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_http_referer: str = "http://localhost:8501"
    openrouter_x_title: str = "TFM-AgriBot"

    # ── Default Models ───────────────────────────────────────────────────
    default_provider: str = "gemini"
    default_model_google: str = "gemini-1.5-flash"
    default_model_openrouter: str = "openai/gpt-4o-mini"

    # ── Ollama Default LLM (Local) ───────────────────────────────────────
    default_ollama_model: str = "qwen2.5:3b"

    # ── Embeddings Configuration ─────────────────────────────────────────
    default_embedding_provider: str = Field(default="ollama", description="Provider for embeddings: ollama or gemini")
    default_embedding_model_cloud: str = "gemini-embedding-001"
    default_embedding_model_local: str = "qwen3-embedding"

    # ── Qdrant LOCAL ─────────────────────────────────────────────────────
    qdrant_local_url: str = "http://localhost:6333"

    # ── Qdrant CLOUD ─────────────────────────────────────────────────────
    qdrant_cloud_url: str = ""
    qdrant_cloud_api_key: Optional[str] = None

    # ── Ollama Configuration (Local) ─────────────────────────────────────
    ollama_base_url: str = "http://localhost:11434"

    # ── Legacy compat: qdrant_url / qdrant_api_key ───────────────────────
    # These are kept for backward compatibility but now resolve dynamically.
    qdrant_url: str = ""
    qdrant_api_key: Optional[str] = None

    @property
    def is_cloud(self) -> bool:
        return self.execution_mode == "cloud"

    @property
    def active_qdrant_url(self) -> str:
        """Returns the Qdrant URL based on execution mode."""
        if self.is_cloud:
            return self.qdrant_cloud_url or self.qdrant_url or "http://localhost:6333"
        return self.qdrant_local_url or self.qdrant_url or "http://localhost:6333"

    @property
    def active_qdrant_api_key(self) -> Optional[str]:
        """Returns the Qdrant API key based on execution mode."""
        if self.is_cloud:
            return self.qdrant_cloud_api_key or self.qdrant_api_key
        return self.qdrant_api_key  # Usually None in local mode

    @property
    def active_embedding_provider(self) -> str:
        """Returns the embedding provider based on configuration."""
        # Check explicit first
        if self.default_embedding_provider:
            return self.default_embedding_provider
            
        if self.is_cloud:
            return "gemini"
        return "ollama"

    @property
    def active_llm_provider(self) -> str:
        """Returns the default LLM provider based on execution mode."""
        if self.is_cloud:
            return self.default_provider  # gemini or openrouter
        return "ollama"

settings = Settings()
