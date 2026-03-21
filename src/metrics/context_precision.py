from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.metrics.judges import JudgeFactory

CONTEXT_PRECISION_PROMPT = """Eres un juez experto evaluando la **Precisión del Contexto** en un sistema RAG.
Tu tarea es analizar una Pregunta y una lista ordenada de Fragmentos de Contexto (recuperados de una base de datos vectorial).

Para cada fragmento, debes determinar si es **Relevante (1)** para responder la pregunta o **No Relevante (0)**.

Pregunta del Usuario:
{question}

Fragmentos de Contexto (En orden de recuperación):
{context_list}

Instrucciones:
1. Revisa cada fragmento uno por uno respetando su índice o posición.
2. Determina si aporta información fáctica o conceptual para armar la respuesta a la pregunta.
3. Responde estrictamente en formato JSON con la lista de relevancia de la misma longitud que el contexto proporcionado.

Formato de SALIDA (JSON ÚNICAMENTE):
{{
    "relevance_list": [1, 0, 1],
    "reason": "Explicación breve de por qué los fragmentos son o no útiles."
}}
"""

class ContextPrecisionMetric:
    def __init__(self, provider: str = None, model_id: str = None):
        self.llm = JudgeFactory.get_judge(provider=provider, model=model_id)
        self.prompt = ChatPromptTemplate.from_template(CONTEXT_PRECISION_PROMPT)
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def evaluate(self, question: str, context_docs: list) -> dict:
        if not context_docs:
            return {"score": 0.0, "reason": "Contexto vacío."}

        # Formatear la lista de forma numerada para que el LLM respete el orden
        context_list_str = ""
        for i, doc in enumerate(context_docs):
            context_list_str += f"Fragmento {i+1}:\n{doc.page_content}\n\n"

        try:
            result = self.chain.invoke({"question": question, "context_list": context_list_str})
            
            relevance_list = result.get("relevance_list", [])
            
            # Si el LLM devolvió un formato incorrecto o vacío, fallback
            if not isinstance(relevance_list, list) or len(relevance_list) == 0:
                 return {"score": 0.0, "reason": "Error en el formato de la lista de relevancia devuelta por el Juez."}

            # Cálculo Matemático: Average Precision (AP)
            # AP = sum(Precision@k * rel_k) / total_relevant
            score = 0.0
            useful_count = 0
            sum_precision = 0.0
            
            for k, rel in enumerate(relevance_list):
                # Asegurar de que sea entero 1 o 0
                is_rel = 1 if rel == 1 or rel is True else 0
                if is_rel:
                    useful_count += 1
                    precision_at_k = useful_count / (k + 1)
                    sum_precision += precision_at_k
            
            if useful_count > 0:
                # Normalizamos por el conteo de útiles encontrados
                score = sum_precision / useful_count
            else:
                score = 0.0

            return {
                "score": round(score, 4),
                "reason": result.get("reason", "Cálculo basado en relevancia secuencial."),
                "relevance_list": relevance_list
            }
        except Exception as e:
            return {"score": 0.0, "reason": f"Error evaluador: {str(e)[:50]}"}
