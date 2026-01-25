from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.metrics.judges import JudgeFactory

FAITHFULNESS_PROMPT = """You are an impartial judge evaluating the "Faithfulness" of an AI Assistant's response.
Faithfulness measures if the response is purely derived from the provided context without hallucinations.

Context:
{context}

Response:
{response}

Task:
1. Identify all claims made in the Response.
2. For each claim, check if it is supported by the Context.
3. Assign a score from 0.0 to 1.0 (1.0 = All claims supported, 0.0 = Pure hallucination).
4. Provide a brief reason.

Output JSON format:
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
            return {"score": 0.0, "reason": "No context or response provided."}
            
        # Flatten context
        context_text = "\n\n".join([f"[{doc.metadata.get('source_id', 'Doc')}]: {doc.page_content}" for doc in context_docs])
        
        try:
            result = self.chain.invoke({"response": response, "context": context_text})
            return result
        except Exception as e:
            return {"score": 0.0, "reason": f"Evaluation error: {e}"}
