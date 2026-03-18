from typing import Any, Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.agent.state import AgentState
from src.chat.rag import RAGEngine
from src.core.providers.factory import ProviderFactory
from src.metrics.faithfulness import FaithfulnessMetric
from src.core.config.settings import settings

class AgentNodes:
    def __init__(self, provider: str = None, model_id: str = None, force_local: bool = False):
        # Inicializar componentes
        # Usamos el provider configurado dinámicamente o por defecto
        
        self.llm = ProviderFactory.get_provider(provider, model_id, force_local=force_local)
        self.rag_engine = RAGEngine()
        self.grader = FaithfulnessMetric() # Usa su propio juez interno

        # Prompt de Generación V2 (más estricto y detallado)
        self.gen_prompt = ChatPromptTemplate.from_template(
            """Eres un Ingeniero Agrónomo Asistente experto en cultivo de arándanos (Blueberries). 
            Tu misión es responder preguntas técnicas basándote estricta y únicamente en el siguiente contexto documental.

            Contexto Documental: 
            {context}
            
            Pregunta Técnica: {question}
            
            Instrucciones Estrictas para Responder:
            1.  **Precisión Técnica**: Si se piden productos químicos, biológicos o métodos, extrae los nombres EXACTOS (Ej: "Abamectina", "Spinosad", "Poda de limpieza").
            2.  **No Generalizar**: Evita respuestas vagas como "usar insecticidas adecuados". Di CUÁLES si el texto lo menciona.
            3.  **Fidelidad Absoluta**: Si el contexto no menciona el tema, responde "No dispongo de información específica sobre [tema] en mi base de conocimientos actual". No inventes.
            4.  **Formato**: Usa listas (bullet points) para enumerar pasos o productos. Se claro y directo.

            Respuesta Detallada:"""
        )
        self.gen_chain = self.gen_prompt | self.llm | StrOutputParser()
        
        # Chains auxiliares
        self.classifier_chain = (
            ChatPromptTemplate.from_template(
                """Clasifica la intención del usuario.
                Query: {question}
                
                Si la query es un saludo (hola, buenos días) o despedida, responde "chitchat".
                Si la query es una pregunta sobre agricultura, arándanos, plagas, o busca información, responde "query".
                
                Salida (solo una palabra):"""
            ) | self.llm | StrOutputParser()
        )

    def classify(self, state: AgentState) -> Dict:
        """Clasifica si es pregunta técnica o charla."""
        print("--- CLASSIFY ---")
        q = state["question"]
        try:
            intent = self.classifier_chain.invoke({"question": q}).strip().lower()
            print(f"   Intent: {intent}")
            if "chitchat" in intent:
                return {"intent": "chitchat"}
            return {"intent": "query"}
        except Exception as e:
            print(f"ERROR en Classify: {e}")
            return {"intent": "query"} # Fallback a RAG

    def respond_chitchat(self, state: AgentState) -> Dict:
        """Responde a saludos sin RAG."""
        print("--- CHITCHAT ---")
        return {"generation": "¡Hola! Soy tu asistente experto en arándanos. ¿En qué puedo ayudarte hoy sobre cultivos o plagas?", "faithfulness_score": 1.0}

    def retrieve(self, state: AgentState) -> Dict:
        """Nodo de recuperación."""
        print(f"--- RETRIEVE: {state['question']} ---")
        docs = self.rag_engine.retrieve_context(state["question"])
        return {"documents": docs, "retry_count": 0}

    def generate(self, state: AgentState) -> Dict:
        """Nodo de generación (con soporte de Self-Correction)."""
        print("--- GENERATE ---")
        docs = state["documents"]
        question = state["question"]
        current_retries = state.get("retry_count", 0)
        feedback = state.get("hallucination_reason", "")
        
        # Formatear contexto simple
        context_str = "\n\n".join([f"- {d.page_content}" for d in docs])
        
        # Si es un reintento, incluyamos feedback
        if current_retries > 0 and feedback:
            print(f"   -> Generando corrección (Intento {current_retries}). Feedback: {feedback}")
            prompt_text = f"""Eres un experto agrónomo. Tu respuesta anterior fue rechazada por falta de fidelidad al contexto o alucinación.
            Crítica del Revisor: {feedback}
            
            Usa el contexto para responder MEJOR, con MÁS PRECISIÓN y FIELMENTE.
            Pregunta: {question}
            Contexto: {context_str}
            Respuesta Corregida:"""
            
            # Ad-hoc chain for correction
            chain = ChatPromptTemplate.from_template(prompt_text) | self.llm | StrOutputParser()
            generation = chain.invoke({}) # Context already baked in prompt string
        else:
            generation = self.gen_chain.invoke({"context": context_str, "question": question})
            
        return {"generation": generation}

    def grade_hallucination(self, state: AgentState) -> Dict:
        """Nodo de evaluación (Self-Reflection)."""
        print("--- GRADE HALLUCINATION ---")
        question = state["question"]
        generation = state["generation"]
        docs = state["documents"]
        
        # Evaluar fidelidad
        result = self.grader.evaluate(generation, docs)
        score = result.get("score", 0.0)
        reason = result.get("reason", "")
        
        print(f"   Score: {score} | Reason: {reason}")
        
        # Gestión de contador de retries
        current_retries = state.get("retry_count", 0)
        if score < 0.8:
            current_retries += 1
            
        return {
            "faithfulness_score": score,
            "hallucination_reason": reason,
            "retry_count": current_retries
        }
