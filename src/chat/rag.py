from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

from src.core.config.settings import settings
from src.core.providers.embeddings import EmbeddingFactory

RAG_PROMPT_TEMPLATE = """You are an expert assistant in blueberry agriculture (arándanos).
Answer the user's question based ONLY on the provided context. 
If the answer is not in the context, say "I don't have enough information in my documents to answer this."

Context:
{context}

Question:
{question}

Instructions:
1. Answer clearly and concisely.
2. Cite the source documents using their ID or title where relevant (e.g., [Source: Title]).
3. If the context contains conflicting information, mention it.
"""

class RAGEngine:
    def __init__(self):
        self.embeddings = EmbeddingFactory.get_embeddings()
        self.client = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
        self.vector_store = QdrantVectorStore(
            client=self.client,
            collection_name="tfm_allucination_v1",
            embedding=self.embeddings
        )
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

    def format_docs(self, docs):
        return "\n\n".join(f"[Source: {d.metadata.get('title', 'Unknown')} (ID: {d.metadata.get('source_id', 'N/A')})]:\n{d.page_content}" for d in docs)

    def get_chain(self, llm):
        prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)
        
        chain = (
            {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        return chain

    def retrieve_context(self, query: str):
        """Helper to inspect retrieved docs directly"""
        return self.retriever.invoke(query)
