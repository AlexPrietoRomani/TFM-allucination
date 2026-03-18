from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.metrics.judges import JudgeFactory

CONTEXT_RELEVANCE_PROMPT = """Eres un juez experto evaluando la Relevancia del Contexto Recuperado.
Tu tarea es determinar si los documentos encontrados por el sistema RAG son útiles y contienen la información necesaria para responder la pregunta del usuario.

Pregunta del Usuario:
{question}

Contexto Recuperado por el Sistema:
{context}

Instrucciones:
1. Lee la Pregunta y el Contexto.
2. Evalúa si el contexto contiene la RESPUESTA a la pregunta.
3. Evalúa si el contexto es PERTINENTE al tema de la pregunta.
4. Asigna un Score de 0.0 a 1.0:
   - 1.0: El contexto contiene la respuesta exacta y completa.
   - 0.5: El contexto es parcialmente relevante o incompleto.
   - 0.0: Contexto irrelevante o desviado.

NOTA: Si el contexto tiene muchas páginas pero contiene la respuesta, ES RELEVANTE (1.0). No penalices por exceso de información si la respuesta está ahí.

Formato de SALIDA (JSON ÚNICAMENTE):
Responde SOLAMENTE con un objeto JSON válido.
{{
    "score": 0.0,
    "reason": "Explicación breve de 1 frase."
}}
"""

class ContextRelevanceMetric:
    def __init__(self, provider: str = None, model_id: str = None):
        self.llm = JudgeFactory.get_judge(provider=provider, model=model_id)
        self.prompt = ChatPromptTemplate.from_template(CONTEXT_RELEVANCE_PROMPT)
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def evaluate(self, question: str, context_docs: list) -> dict:
        if not context_docs:
            return {"score": 0.0, "reason": "No se recuperaron documentos (Contexto vacío implica relevancia cero)."}
            
        context_text = "\n\n".join([f"Documento ID {doc.metadata.get('source_id', 'Desc')}: {doc.page_content}" for doc in context_docs])
        
        try:
            result = self.chain.invoke({"question": question, "context": context_text})
            # Validación
            if "score" not in result:
                result["score"] = 0.0
            if "reason" not in result:
                result["reason"] = "Error formato JSON"
            return result
        except Exception as e:
            return {"score": 0.0, "reason": f"Error evaluador: {str(e)[:50]}"}
