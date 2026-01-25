from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

from src.core.config.settings import settings
from src.core.providers.embeddings import EmbeddingFactory

class RAGEngine:
    def __init__(self):
        # 1. Configurar Embeddings (mismo que indexación)
        self.embeddings = EmbeddingFactory.get_embeddings()
        
        # 2. Conectar a Qdrant (modo lectura)
        self.vector_store = QdrantVectorStore(
            client=QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key),
            collection_name="tfm_allucination_v1",
            embedding=self.embeddings
        )
        
        # 3. Configurar Retriever
        # 'k': número de documentos a recuperar. Ajustable.
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 5})

    def get_chain(self, llm):
        """
        Construye la cadena RAG completa:
        Retriever -> Format -> Prompt -> LLM -> Parser
        """
        
        # Prompt de Sistema (Ingeniería de Prompts para reducir alucinación)
        template = """Eres un asistente agrícola experto en manejo de arándanos.
        Usa SOLAMENTE el siguiente contexto para responder a la pregunta.
        
        Reglas:
        1. Si la respuesta no está en el contexto, di "No tengo suficiente información en mis documentos".
        2. NO inventes información.
        3. Cita la fuente (título o ID del documento) si es posible.
        
        Contexto:
        {context}
        
        Pregunta: {question}
        """
        
        prompt = ChatPromptTemplate.from_template(template)
        
        def format_docs(docs):
            return "\n\n".join([f"[Fuente: {d.metadata.get('title', 'Doc')}, ID: {d.metadata.get('source_id')}]\n{d.page_content}" for d in docs])

        # Cadena LCEL (LangChain Expression Language)
        rag_chain = (
            {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        
        return rag_chain

    def retrieve_context(self, query: str):
        """Método helper para obtener documentos raw (para UI o debugging)."""
        return self.retriever.invoke(query)
