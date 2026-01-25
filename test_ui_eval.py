
import asyncio
import pandas as pd
from src.core.providers.factory import ProviderFactory
from src.chat.rag import RAGEngine
from eval.run_eval import evaluate_row_v0_v1
from eval.run_eval_v2 import evaluate_row_v2
from src.agent.graph import AgentGraph

# Mock objects
class MockLLM:
    def invoke(self, *args, **kwargs):
        class Resp:
            content = "Mock Response"
        return Resp()

class MockRAGEngine:
    def get_chain(self, llm):
        class Chain:
            def invoke(self, q):
                return "Mock RAG Response"
        return Chain()

class MockAgent:
    class App:
        async def ainvoke(self, inputs):
            return {
                "generation": "Mock Agent Response",
                "faithfulness_score": 0.9,
                "retry_count": 0
            }
    app = App()

async def test():
    print("Testing Eval Integration...")
    
    row = {"id": "test", "question": "test question"}
    
    # Test V0/V1
    print("Testing V0/V1 logic...")
    res1 = evaluate_row_v0_v1(row, MockLLM(), MockRAGEngine().get_chain(None), "test", "test")
    print("V0/V1 Result:", res1)
    
    # Test V2
    print("Testing V2 logic...")
    res2 = await evaluate_row_v2(row, MockAgent())
    print("V2 Result:", res2)
    
    print("Integration Test Passed!")

if __name__ == "__main__":
    asyncio.run(test())
