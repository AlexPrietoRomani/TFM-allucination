from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.metrics.judges import JudgeFactory

CONTEXT_RELEVANCE_PROMPT = """You are an impartial judge evaluating "Context Relevance".
This measures if the retrieved documents contain the information needed to answer the user's question.

Question:
{question}

Retrieved Context:
{context}

Task:
1. Read the Question.
2. Read the Context.
3. Determine if the Context contains the answer.
4. Assign a score from 0.0 to 1.0 (1.0 = Perfect context, 0.0 = Irrelevant context).
5. Provide a brief reason.

Output JSON format:
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
            return {"score": 0.0, "reason": "No context retrieved."}
            
        context_text = "\n\n".join([f"[{doc.metadata.get('source_id', 'Doc')}]: {doc.page_content}" for doc in context_docs])
        
        try:
            result = self.chain.invoke({"question": question, "context": context_text})
            return result
        except Exception as e:
            return {"score": 0.0, "reason": f"Evaluation error: {e}"}
