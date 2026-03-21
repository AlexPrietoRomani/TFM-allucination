"""
test_ui_eval.py — Pruebas de Integración y Mock para la Interfaz (UI)

Simula llamadas Async generadoras al app y evalua el comportamiento del flujo V2 
de los agentes en Streamlit con mocks dinámicos de respuestas.
"""

import asyncio
import pandas as pd
import sys
import os

# Add root to pythonpath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.providers.factory import ProviderFactory
from src.chat.rag import RAGEngine
try:
    from eval.run_eval import evaluate_row_v0_v1
    from eval.run_eval_v2 import evaluate_row_v2
except ImportError:
    print("Eval modules not found, skipping specific eval tests")

# Mock objects improved for Async Generator (astream_events)
class MockAgent:
    class MockApp:
        async def ainvoke(self, inputs):
            return {
                "generation": "Mock Agent Response",
                "documents": [{"page_content": "doc1", "metadata": {"source_id": "test"}}],
                "faithfulness_score": 0.9,
                "retry_count": 0
            }
        
        async def astream_events(self, inputs, version):
            # Simulate events
            yield {"event": "on_chain_start", "name": "retrieve"}
            yield {"event": "on_chain_end", "name": "retrieve", "data": {"output": {"documents": [{"page_content": "doc1", "metadata": {"source_id": "test"}}]}}}
            yield {"event": "on_chain_start", "name": "generate"}

    app = MockApp()

async def test_integration():
    print("Testing Eval Integration Sync/Async...")
    
    # Mock row
    row = pd.Series({"id": "test", "question": "test question"})
    
    # Test V2 logic
    print("Testing V2 logic...")
    try:
        from src.ui.utils import run_agent_v2
        # Test UI util wrapper
        resp, docs, steps = await run_agent_v2(MockAgent(), "test question")
        assert resp == "Mock Agent Response"
        assert len(docs) == 1
        print("V2 Agent UI Wrapper: OK")
        
    except Exception as e:
        print(f"V2 Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_integration())
