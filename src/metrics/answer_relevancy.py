from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.metrics.judges import JudgeFactory

ANSWER_RELEVANCY_PROMPT = """Eres un juez experto evaluando la **Relevancia de la Respuesta** en un sistema RAG de Agronomía.
Tu tarea es determinar si la Respuesta del asisente ataca directamente la Pregunta del usuario sin dar vueltas ni incluir información que no aporta.

Pregunta del Usuario:
{question}

Respuesta del Asistente:
{response}

Instrucciones de Evaluación:
1. Evalúa si la respuesta resuelve la duda planteada.
2. Evalúa si la respuesta contiene detalles irrelevantes o "relleno" que no guardan relación con la pregunta.
3. Asigna un Score de 0.0 a 1.0:
    - 1.0: La respuesta es concisa, directa y aborda el 100% de la pregunta.
    - 0.5: La respuesta es parcialmente relevante, divaga o no responde el núcleo de la duda.
    - 0.0: La respuesta no tiene nada que ver con la pregunta o es completamente evasiva.

Formato de SALIDA (JSON ÚNICAMENTE):
{{
    "score": 0.0,
    "reason": "Explicación breve de 1 frase justificando el puntaje."
}}
"""

class AnswerRelevancyMetric:
    def __init__(self, provider: str = None, model_id: str = None):
        self.llm = JudgeFactory.get_judge(provider=provider, model=model_id)
        self.prompt = ChatPromptTemplate.from_template(ANSWER_RELEVANCY_PROMPT)
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def evaluate(self, question: str, response: str) -> dict:
        if not question or not response:
            return {"score": 0.0, "reason": "Faltan datos de Entrada (Pregunta o Respuesta vacías)."}

        try:
            # Invocar cadena
            result = self.chain.invoke({"question": question, "response": response})
            # Validación básica de estructura
            if "score" not in result:
                result["score"] = 0.0
            if "reason" not in result:
                result["reason"] = "Error formato JSON"
            return result
        except Exception as e:
            return {"score": 0.0, "reason": f"Error evaluador: {str(e)[:50]}"}
