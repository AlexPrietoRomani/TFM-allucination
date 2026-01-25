from typing import List, TypedDict, Optional
from langchain_core.documents import Document

class AgentState(TypedDict):
    """
    Estado del grafo del Agente RAG con Auto-Corrección.
    """
    question: str
    documents: List[Document]
    generation: str
    
    # Métricas y control de flujo
    faithfulness_score: float
    hallucination_reason: str
    retry_count: int
    intent: str # 'query' o 'chitchat'
    
    # Flags opcionales para UI
    status: str
