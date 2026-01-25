from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.metrics.judges import JudgeFactory

FAITHFULNESS_PROMPT = """Eres un juez imparcial evaluando la "Fidelidad" de la respuesta de un Asistente IA.
La Fidelidad mide si la respuesta se deriva puramente del contexto proporcionado, sin alucinaciones.

Contexto:
{context}

Respuesta:
{response}

Tarea:
1. Identifica todas las afirmaciones hechas en la Respuesta.
2. Para cada afirmación, verifica si está soportada por el Contexto.
3. Asigna un puntaje de 0.0 a 1.0 (1.0 = Todas las afirmaciones soportadas, 0.0 = Alucinación pura).
4. Provee una razón breve.

Formato de salida JSON:
{{
    "score": <float>,
    "reason": "<string>"
}}
"""

class FaithfulnessMetric:
    def __init__(self):
        self.llm = JudgeFactory.get_judge()
        self.prompt = ChatPromptTemplate.from_template(FAITHFULNESS_PROMPT)
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def evaluate(self, response: str, context_docs: list) -> dict:
        if not context_docs or not response:
            return {"score": 0.0, "reason": "No se proporcionó contexto o respuesta."}
            
        # Aplanar contexto
        context_text = "\n\n".join([f"[{doc.metadata.get('source_id', 'Doc')}]: {doc.page_content}" for doc in context_docs])
        
        try:
            result = self.chain.invoke({"response": response, "context": context_text})
            return result
        except Exception as e:
            return {"score": 0.0, "reason": f"Error de evaluación: {e}"}
