import pytest
import os
from src.core.config.settings import settings
from src.core.providers.factory import ProviderFactory

# Skip tests if API keys are not present (mocking would be better for CI, but this is smoke testing connectivity)
SKIP_GEMINI = not settings.google_api_key
SKIP_OPENROUTER = not settings.openrouter_api_key

@pytest.mark.skipif(SKIP_GEMINI, reason="GOOGLE_API_KEY not set")
def test_gemini_smoke():
    try:
        llm = ProviderFactory.get_provider("gemini", "gemini-1.5-flash")
        response = llm.invoke("Hello, answer with PONG")
        assert response is not None
        assert response.content is not None
        print(f"Gemini response: {response.content}")
    except Exception as e:
        pytest.fail(f"Gemini smoke test failed: {e}")

@pytest.mark.skipif(SKIP_OPENROUTER, reason="OPENROUTER_API_KEY not set")
def test_openrouter_smoke():
    try:
        # Use a cheap/free model for testing if possible, or standard one
        llm = ProviderFactory.get_provider("openrouter", "google/gemini-pro-1.5-exp") 
        # Using a model likely to exist on OpenRouter. Ideally should come from registry.
        
        response = llm.invoke("Hello, answer with PONG")
        assert response is not None
        assert response.content is not None
        print(f"OpenRouter response: {response.content}")
    except Exception as e:
        pytest.fail(f"OpenRouter smoke test failed: {e}")

def test_factory_invalid_provider():
    with pytest.raises(ValueError):
        ProviderFactory.get_provider("invalid_provider", "model")
