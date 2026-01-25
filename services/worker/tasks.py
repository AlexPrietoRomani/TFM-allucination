import os
from redis import Redis
from rq import Queue
from src.metrics.factscore import FactScoreMetric
from langchain_core.documents import Document

# Configuración Redis
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_conn = Redis(host=REDIS_HOST, port=REDIS_PORT)
queue = Queue(connection=redis_conn)

def calculate_factscore_task(response_text: str, context_docs_serializable: list):
    """
    Ejecuta el cálculo de FactScore en Background.
    
    Args:
        response_text (str): Respuesta del LLM.
        context_docs_serializable (list): Lista de dicts {'page_content': str, 'metadata': dict}.
    """
    print(f"👷 Worker: Iniciando cálculo FactScore para respuesta de {len(response_text)} chars...")
    
    try:
        # Rehidratar Objetos Document
        docs = [
            Document(page_content=d['page_content'], metadata=d.get('metadata', {})) 
            for d in context_docs_serializable
        ]
        
        metric = FactScoreMetric()
        result = metric.calculate(response_text, docs)
        
        print(f"✅ Worker: FactScore terminado. Score: {result.get('score')}")
        return result
        
    except Exception as e:
        print(f"❌ Worker Error: {e}")
        return {"error": str(e), "score": 0.0}
