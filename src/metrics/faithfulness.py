from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.metrics.judges import JudgeFactory

FAITHFULNESS_PROMPT = """Eres un juez experto e imparcial evaluando la "Fidelidad" de un Asistente de IA Agrícola.
Tu objetivo es determinar si la respuesta del asistente se basa en el contexto proporcionado, sin inventar información.

Contexto Recuperado:
{context}

Respuesta del Asistente:
{response}

Instrucciones de Evaluación:
1. Analiza si las afirmaciones clave de la Respuesta están respaldadas por el Contexto.
2. Sé razonable: si el asistente parafrasea o resume correctamente el contexto, cuenta como VÁLIDO.
3. Penaliza solo si hay información contradictoria o inventada que no aparece en el contexto.
4. Asignar un puntaje (score) entre 0.0 y 1.0.
   - 1.0: Totalmente fiel al contexto.
   - 0.5: Parcialmente fiel (mezcla datos reales e inventados).
   - 0.0: Alucinación total o irrelevante.

Formato de SALIDA (JSON ÚNICAMENTE):
Responde SOLAMENTE con un objeto JSON válido, sin texto adicional antes ni después.
{{
    "score": 0.0,
    "reason": "Explicación breve de 1 frase."
}}
"""

class FaithfulnessMetric:
    def __init__(self, provider: str = None, model_id: str = None):
        self.llm = JudgeFactory.get_judge(provider=provider, model=model_id)
        self.prompt = ChatPromptTemplate.from_template(FAITHFULNESS_PROMPT)
        self.chain = self.prompt | self.llm | JsonOutputParser()

    def evaluate(self, response: str, context_docs: list) -> dict:
        if not context_docs or not response:
            return {"score": 0.0, "reason": "No se proporcionó contexto o respuesta para evaluar."}
            
        # Aplanar contexto con formato claro
        context_text = "\n\n".join([f"Documento ID {doc.metadata.get('source_id', 'Desc')}: {doc.page_content}" for doc in context_docs])
        
        try:
            # Invocar cadena
            result = self.chain.invoke({"response": response, "context": context_text})
            # Validación básica de estructura
            if "score" not in result:
                result["score"] = 0.0
            if "reason" not in result:
                result["reason"] = "Error formato JSON"
            return result
        except Exception as e:
            # Fallback robusto
            return {"score": 0.0, "reason": f"Error evaluador: {str(e)[:50]}"}
