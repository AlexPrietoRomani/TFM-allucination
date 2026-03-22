"""
test_agent_v2.py — Test de Preguntas del Agente LangGraph (V2)

Inicia el grafo del agente (AgentGraph) y dispara un listado de preguntas 
de prueba para observar las respuestas generadas y sus scores de alucinación.

Uso:
    uv run python tests/test_agent_v2.py
"""

import asyncio
from src.agent.graph import AgentGraph

async def main():
    print("Inicializando Agente V2 (LangGraph)...")
    agent = AgentGraph()
    
    questions = [
        "Hola, buenas tardes",
        "En los Lineamientos SAG 2015, ¿cada cuántos días es el monitoreo de Diaporthe vaccinii?"
    ]
    
    for q in questions:
        print(f"\n--- Probando Pregunta: {q} ---")
        result = await agent.app.ainvoke({"question": q})
        print(f"Respuesta: {result.get('generation')}")
        print(f"Score: {result.get('faithfulness_score', 'N/A')}")
        print(f"Retries: {result.get('retry_count', 0)}")

if __name__ == "__main__":
    asyncio.run(main())
