from typing import List, Dict
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.metrics.judges import JudgeFactory

# 1. Prompt para extraer afirmaciones atómicas
ATOMIC_CLAIMS_PROMPT = """Eres un experto lingüista. Tu tarea es descomponer una respuesta compleja en una lista de "afirmaciones atómicas" (atomic claims).
Una afirmación atómica es una sentencia simple, indivisible, que contiene un solo hecho verificable.

Respuesta Original:
{response}

Instrucciones:
1. Divide la respuesta en oraciones simples.
2. Asegúrate de que cada afirmación sea autónoma (resuelve pronombres como "él" o "esto").
3. Ignora saludos o frases de cortesía.
4. Salida en formato JSON puro: una lista de strings.

Ejemplo:
Respuesta: "El monitoreo se hace cada 7 días y debe ser a 20cm."
Salida: ["El monitoreo se hace cada 7 días.", "El monitoreo debe ser a 20cm."]

Salida JSON:
"""

# 2. Prompt para verificar cada afirmación contra el contexto
VERIFICATION_PROMPT = """Eres un verificador de hechos (Fact-Checker) imparcial.
Debes verificar si una afirmación (Claim) está soportada por la Evidencia (Contexto).

Afirmación: {claim}
Contexto: {context}

Etiquetas posibles:
- "Soportado": La afirmación es totalmente consistente con el contexto.
- "Contradicho": El contexto dice algo diferente u opuesto.
- "NoVerificado": El contexto no menciona información sobre esto.

Salida JSON:
{{
    "label": "Soportado" | "Contradicho" | "NoVerificado",
    "reason": "Explicación breve"
}}
"""

class FactScoreMetric:
    def __init__(self, provider: str = None, model_id: str = None):
        # Usamos el juez configurado (Ollama/Gemini/OpenRouter) pasando los parametros
        self.llm = JudgeFactory.get_judge(provider=provider, model=model_id)
        
        # Cadenas
        self.extractor_chain = (
            ChatPromptTemplate.from_template(ATOMIC_CLAIMS_PROMPT) 
            | self.llm 
            | JsonOutputParser()
        )
        
        self.verifier_chain = (
            ChatPromptTemplate.from_template(VERIFICATION_PROMPT)
            | self.llm
            | JsonOutputParser()
        )

    def extract_claims(self, response: str) -> List[str]:
        """Extrae lista de hechos atómicos de la respuesta."""
        if not response or len(response.strip()) < 5:
            return []
        try:
            claims = self.extractor_chain.invoke({"response": response})
            if isinstance(claims, list):
                return claims
            # Fallback si el modelo devuelve dict
            return claims.get("claims", [])
        except Exception as e:
            print(f"Error extrayendo claims: {e}")
            return []

    def verify_claim(self, claim: str, context_text: str) -> Dict:
        """Verifica un solo hecho."""
        try:
            return self.verifier_chain.invoke({"claim": claim, "context": context_text})
        except Exception as e:
            return {"label": "Error", "reason": str(e)}

    def calculate(self, response: str, context_docs: list) -> Dict:
        """
        Ejecuta el pipeline completo FactScore.
        Retorna score y desglose.
        """
        # 1. Preparar contexto
        if not context_docs:
            return {"score": 0.0, "breakdown": [], "error": "No hay contexto"}
            
        context_text = "\n\n".join([d.page_content for d in context_docs])
        
        # 2. Extraer
        claims = self.extract_claims(response)
        if not claims:
            return {"score": 0.0, "total_claims": 0, "breakdown": []}
            
        # 3. Verificar cada uno
        verified_claims = []
        supported_count = 0
        
        print(f"    - Verificando {len(claims)} hechos atómicos...")
        
        for claim in claims:
            res = self.verify_claim(claim, context_text)
            label = res.get("label", "NoVerificado")
            
            verified_claims.append({
                "claim": claim,
                "label": label,
                "reason": res.get("reason", "")
            })
            
            if label == "Soportado":
                supported_count += 1
                
        # 4. Calcular FactScore
        score = supported_count / len(claims) if claims else 0.0
        
        return {
            "score": score,
            "total_claims": len(claims),
            "supported_claims": supported_count,
            "breakdown": verified_claims
        }
