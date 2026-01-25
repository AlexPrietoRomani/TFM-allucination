from langgraph.graph import StateGraph, END
from src.agent.state import AgentState
from src.agent.nodes import AgentNodes

class AgentGraph:
    def __init__(self):
        self.nodes = AgentNodes()
        self.workflow = StateGraph(AgentState)
        
        # 1. Añadir Nodos
        self.workflow.add_node("classify", self.nodes.classify)
        self.workflow.add_node("chitchat", self.nodes.respond_chitchat)
        self.workflow.add_node("retrieve", self.nodes.retrieve)
        self.workflow.add_node("generate", self.nodes.generate)
        self.workflow.add_node("grade", self.nodes.grade_hallucination)
        
        # 2. Definir flujo
        self.workflow.set_entry_point("classify")
        
        # Routing desde classify
        self.workflow.add_conditional_edges(
            "classify",
            self.route_intent,
            {
                "chitchat": "chitchat",
                "query": "retrieve"
            }
        )
        
        self.workflow.add_edge("chitchat", END)
        self.workflow.add_edge("retrieve", "generate")
        self.workflow.add_edge("generate", "grade")
        
        # 3. Transición Condicional (Loop)
        self.workflow.add_conditional_edges(
            "grade",
            self.decide_next_step,
            {
                "useful": END,
                "hallucination": "generate", # Loop back to generate
                "max_retries": END
            }
        )
        
        self.app = self.workflow.compile()

    def route_intent(self, state: AgentState) -> str:
        return state.get("intent", "query")

    def decide_next_step(self, state: AgentState) -> str:
        """Determina si la respuesta es aceptable o necesita corrección."""
        score = state.get("faithfulness_score", 0.0)
        retries = state.get("retry_count", 0)
        
        LIMIT_RETRIES = 1 # Solo 1 intento de corrección para no eternizar
        THRESHOLD = 0.8
        
        if score >= THRESHOLD:
            print("--- DECISION: USEFUL (Pass) ---")
            return "useful"
        
        if retries >= LIMIT_RETRIES:
            print("--- DECISION: MAX RETRIES REACHED (Stop) ---")
            return "max_retries"
            
        # Si falla y tenemos intentos, incrementamos contador
        # Nota: En StateGraph inmutable, idealmente retornaríamos el update,
        # pero aquí solo decidimos el route. El state update debe hacerse en el nodo.
        # LangGraph moderno permite updates en nodos. Necesitamos un nodo de "Update Retry" o hacerlo en grade.
        # Asumiremos que 'grade' o un nodo intermedio actualiza el retry. 
        # Modificaré nodes.py para que 'grade' maneje el incremento o crearé un nodo 'prepare_retry'.
        
        print("--- DECISION: HALLUCINATION (Retry) ---")
        return "hallucination"
