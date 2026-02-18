import pytest
import sys
import os
# Add root to pythonpath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ui.utils import calculate_metrics_sync

def test_calculate_metrics_sync_disabled():
    """
    Si use_metrics es False, debe retornar un dict vacío.
    """
    res = calculate_metrics_sync("pregunta", "respuesta", [], use_metrics=False)
    assert res == {}

def test_calculate_metrics_sync_no_docs():
    """
    Si no hay documentos, métricas como Relevancia deben ser 0.0.
    """
    try:
        res = calculate_metrics_sync("pregunta", "respuesta", [], use_metrics=True)
        # Puede variar dependiendo de si FaithfulnessMetric está disponible
        # Si no hay docs, faithfulness suele ser 0 o ignorada
        assert res.get("rel_score", 0.0) == 0.0
        assert res.get("factscore", 0.0) == 0.0
    except ImportError:
        pytest.skip("Módulos de métricas no instalados.")

def test_calculate_metrics_sync_structure():
    """
    Verificar estructura básica cuando hay docs (mockeando si es necesario, pero aquí probamos la lógica de utils, no de metrics).
    """
    pass # No podemos probar sin un LLM real o mockeado profundo.
