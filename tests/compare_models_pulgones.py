import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chat.rag import RAGEngine
from src.agent.graph import AgentGraph
from src.core.providers.factory import ProviderFactory

QUESTION = "como puedo combatir con los pulgones en mi huerto?, dime los ingredientes activos que puedo utilizar"

async def run_comparison():
    output = []
    output.append(f"PREGUNTA: {QUESTION}\n")
    
    models = ["qwen2.5:3b", "llama3.2:latest"]
    
    rag = RAGEngine()
    
    for model in models:
        output.append(f"\n========================================\nMODELO: {model}\n========================================")
        
        try:
            llm = ProviderFactory.get_provider("ollama", model)
            
            # V1
            chain = rag.get_chain(llm)
            try:
                res_v1 = chain.invoke(QUESTION)
                output.append("\n[V1 RAG]:\n" + res_v1)
            except Exception as e:
                output.append(f"\n[V1 Error]: {e}")
                
            # V2
            agent = AgentGraph("ollama", model)
            try:
                state = await agent.app.ainvoke({"question": QUESTION})
                res_v2 = state.get("generation", "Error Gen")
                output.append("\n[V2 Agente]:\n" + res_v2)
                output.append(f"\n[V2 Score]: {state.get('faithfulness_score')}")
            except Exception as e:
                output.append(f"\n[V2 Error]: {e}")
                
        except Exception as e:
            output.append(f"Error {model}: {e}")
            
    with open("tests/comparativa_pulgones.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    asyncio.run(run_comparison())
