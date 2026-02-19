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
        
        # Prompt de Sistema MEJORADO (Ingeniería de Prompts para reducir alucinación y aumentar detalle)
        template = """Eres un Ingeniero Agrónomo experto y preciso especializado en el cultivo de arándanos.
        Tu objetivo es responder a la consulta del usuario basándote ÚNICA y EXCLUSIVAMENTE en la información proporcionada en el siguiente contexto.

        Contexto Recuperado:
        {context}
        
        Consulta del Usuario: {question}

        Instrucciones Obligatorias:
        1.  **Especificidad ante todo**: Si el usuario pide ingredientes activos, productos, dosis o métodos, extrae los nombres EXACTOS del contexto. No generalices (ej: di "Spinosad" en vez de "insecticida biológico" si el texto lo dice).
        2.  **Cita de Fuentes**: Al final de cada afirmación importante, indica la fuente entre corchetes, ej: [Fuente: Manejo Plagas 2024].
        3.  **Honestidad Radical**: Si el contexto no contiene la respuesta exacta a lo que se pregunta, di: "La información disponible en mis documentos no cubre específicamente [tema solicitado]". NO inentes rellenar con conocimiento externo.
        4.  **Estructura**: Usa viñetas o listas para enumerar pasos, productos o síntomas.

        Respuesta Técnica:"""
        
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
