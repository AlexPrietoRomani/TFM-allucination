import json
from pathlib import Path
from typing import Any, List, Dict
from tenacity import retry, wait_exponential, stop_after_attempt

from src.core.providers.gemini import GeminiProvider
from src.core.providers.openrouter import OpenRouterProvider
from src.core.providers.ollama import OllamaProvider
from src.core.config.settings import settings

REGISTRY_PATH = Path("src/core/config/model_registry.json")

class ProviderFactory:
    _models_cache: Dict[str, Any] = {}

    @classmethod
    def _load_registry(cls):
        """Carga el registro de modelos JSON si no ha sido cargado aún."""
        if cls._models_cache:
            return

        if REGISTRY_PATH.exists():
            try:
                with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # La estructura es {\"providers\": {\"gemini\": [...], \"openrouter\": [...]}}
                    providers_data = data.get("providers", {})
                    for provider_key, models_list in providers_data.items():
                        for m in models_list:
                            cls._models_cache[m["id"]] = m
            except Exception as e:
                print(f"Advertencia: Falló al cargar registro de modelos: {e}")
        else:
            print(f"Advertencia: Registro de modelos no encontrado en {REGISTRY_PATH}")

    @classmethod
    def validate_model(cls, model_name: str) -> bool:
        """
        Verifica si el modelo existe en el registro. 
        Retorna True si se encuentra o si falta el registro (modo permisivo).
        """
        cls._load_registry()
        if not cls._models_cache:
            # Si el registro falta o está vacío, permitir todo (fail open).
            # Dado el entorno dinámico, es más seguro para desarrollo.
            return True

        if model_name not in cls._models_cache:
            # Log de advertencia pero permitir proceder (útil para modelos locales/custom)
            return False
        return True

    @staticmethod
    def get_provider(provider_name: str, model_name: str, force_local: bool = False, **kwargs) -> Any:
        """
        Fábrica principal: Retorna una instancia configurada de ChatModel (LangChain)
        según el proveedor solicitado.
        
        En modo cloud, si se pide 'ollama' se emite una advertencia y se redirige
        al proveedor cloud configurado (salvo que force_local=True).
        """
        # Validar (solo loguea advertencia por ahora)
        ProviderFactory.validate_model(model_name)

        # Normalizar nombre del proveedor
        provider_name = provider_name.lower().strip()

        # Guardia: en modo cloud, redirigir ollama al proveedor cloud
        if settings.is_cloud and provider_name == "ollama" and not force_local:
            fallback = settings.active_llm_provider
            print(f"⚠ Modo CLOUD activo: redirigiendo 'ollama' → '{fallback}'")
            provider_name = fallback
            # Ajustar model_name a uno compatible con cloud
            if fallback == "gemini":
                model_name = model_name if "gemini" in model_name else settings.default_model_google
            elif fallback == "openrouter":
                model_name = model_name if "/" in model_name else settings.default_model_openrouter

        if provider_name == "gemini":
            return GeminiProvider.get_chat_model(model_name, **kwargs)
        elif provider_name == "openrouter":
            return OpenRouterProvider.get_chat_model(model_name, **kwargs)
        elif provider_name == "ollama":
            return OllamaProvider.get_chat_model(model_name, **kwargs)
        else:
            raise ValueError(f"Proveedor desconocido: {provider_name}")
