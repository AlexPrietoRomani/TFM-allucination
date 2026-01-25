from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.metrics.judges import JudgeFactory

CONTEXT_RELEVANCE_PROMPT = """Eres un juez imparcial evaluando la "Relevancia del Contexto".
Esto mide si los documentos recuperados contienen la información necesaria para responder la pregunta del usuario.

Pregunta:
{question}

Contexto Recuperado:
{context}

Tarea:
1. Lee la Pregunta.
2. Lee el Contexto.
3. Determina si el Contexto contiene la respuesta.
4. Asigna un puntaje de 0.0 a 1.0 (1.0 = Contexto perfecto, 0.0 = Contexto irrelevante).
5. Provee una razón breve.

Formato de salida JSON:
{{
    "score": <float>,
    "reason": "<string>"
}}
"""

class ContextRelevanceMetric:
    def __init__(self):
        self.llm = JudgeFactory.get_judge()
        self.prompt = ChatPromptTemplate.from_template(CONTEXT_RELEVANCE_PROMPT)
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def evaluate(self, question: str, context_docs: list) -> dict:
        if not context_docs:
            return {"score": 0.0, "reason": "No se recuperó contexto."}
            
        context_text = "\n\n".join([f"[{doc.metadata.get('source_id', 'Doc')}]: {doc.page_content}" for doc in context_docs])
        
        try:
            result = self.chain.invoke({"question": question, "context": context_text})
            return result
        except Exception as e:
            return {"score": 0.0, "reason": f"Error de evaluación: {e}"}
