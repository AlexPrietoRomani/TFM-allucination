import pytest
import os
from src.core.config.settings import settings
from src.core.providers.factory import ProviderFactory

# Saltar pruebas si las claves API no están presentes (mocking sería mejor para CI, pero esto es humo de conectividad)
SKIP_GEMINI = not settings.google_api_key
SKIP_OPENROUTER = not settings.openrouter_api_key

@pytest.mark.skipif(SKIP_GEMINI, reason="GOOGLE_API_KEY no establecida")
def test_gemini_smoke():
    try:
        # Usar modelo por defecto configurado para Gemini
        model = settings.default_model_google
        print(f"Probando Gemini con modelo: {model}")
        llm = ProviderFactory.get_provider("gemini", model)
        response = llm.invoke("Hola, responde con PONG")
        assert response is not None
        assert response.content is not None
        print(f"Respuesta Gemini: {response.content}")
    except Exception as e:
        pytest.fail(f"Prueba de humo Gemini falló: {e}")

@pytest.mark.skipif(SKIP_OPENROUTER, reason="OPENROUTER_API_KEY no establecida")
def test_openrouter_smoke():
    try:
        # Usar modelo por defecto configurado para OpenRouter
        model = settings.default_model_openrouter
        print(f"Probando OpenRouter con modelo: {model}")
        llm = ProviderFactory.get_provider("openrouter", model) 
        
        response = llm.invoke("Hola, responde con PONG")
        assert response is not None
        assert response.content is not None
        print(f"Respuesta OpenRouter: {response.content}")
    except Exception as e:
        pytest.fail(f"Prueba de humo OpenRouter falló: {e}")

def test_factory_invalid_provider():
    with pytest.raises(ValueError):
        ProviderFactory.get_provider("proveedor_invalido", "modelo")
