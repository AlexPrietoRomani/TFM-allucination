import streamlit as st
import json
import time
from pathlib import Path
from src.core.providers.factory import ProviderFactory
from src.core.config.settings import settings
from src.chat.rag import RAGEngine
from langchain_core.messages import HumanMessage, AIMessage

# Page Config
st.set_page_config(
    page_title="TFM Chatbot (V0 vs V1)",
    page_icon="🫐",
    layout="wide"
)

# Load Registry
REGISTRY_PATH = Path("src/core/config/model_registry.json")

@st.cache_data
def load_model_registry():
    if not REGISTRY_PATH.exists():
        return {}
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

registry = load_model_registry()

# Initialize RAG Engine
@st.cache_resource
def get_rag_engine():
    return RAGEngine()

rag_engine = get_rag_engine()

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuración")
    
    # Provider/Model Selector
    # providers = list(registry.get("providers", {}).keys()) if registry else ["gemini", "openrouter"]
    # Add manual Ollama support
    providers = ["gemini", "openrouter", "ollama"]
    
    provider = st.selectbox("Proveedor", providers, index=0)
    
    if provider == "ollama":
        model_id = st.text_input("Modelo Ollama", value="gpt-oss:20b", help="Nombre exacto del modelo (ej: gpt-oss:20b, llama3)")
    else:
        # Load from registry for others
        available_models = [m["id"] for m in registry.get("providers", {}).get(provider, [])]
        
        # Default logic
        default_model = settings.default_model_google if provider == "gemini" else settings.default_model_openrouter
        try:
            def_index = available_models.index(default_model)
        except ValueError:
            def_index = 0
            
        model_id = st.selectbox("Modelo", available_models, index=def_index)
    
    st.divider()
    if st.button("🗑️ Limpiar Historial"):
        st.session_state.messages = []
        st.rerun()

st.title("🫐 TFM Chatbot: Comparativa V0 vs V1")
st.markdown("Comparación en tiempo real: **Baseline (V0)** vs **RAG (V1)**")

# Display History
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        # Comparison response
        with st.chat_message("assistant"):
            if "v0" in msg:
                st.markdown("### ⚖️ Comparativa Histórica")
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### V0 (Sin RAG)")
                    st.caption(f"⏱️ {msg['time_v0']:.2f}s")
                    st.markdown(
                        f"""<div style="height: 300px; overflow-y: auto; background-color: #262730; padding: 10px; border-radius: 5px; border: 1px solid #4a4a4a;">{msg['v0']}</div>""",
                        unsafe_allow_html=True
                    )
                with col2:
                    st.markdown("#### V1 (Con RAG)")
                    st.caption(f"⏱️ {msg['time_v1']:.2f}s")
                    st.markdown(
                        f"""<div style="height: 300px; overflow-y: auto; background-color: #1e1e1e; padding: 10px; border-radius: 5px; border: 1px solid #4a4a4a;">{msg['v1']}</div>""",
                        unsafe_allow_html=True
                    )
                    
                    if "sources" in msg and msg["sources"]:
                        st.markdown("**Fuentes (V1):**")
                        for i, doc in enumerate(msg["sources"]):
                            with st.expander(f"{i+1}. {doc.metadata.get('title', 'Doc')}"):
                                st.caption(f"ID: {doc.metadata.get('source_id')}")
                                st.markdown(f"*{doc.page_content[:300]}...*")

# Input
if prompt := st.chat_input("Pregunta sobre manejo de arándanos..."):
    # Add User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        status = st.status("Generando respuestas...")
        
        try:
            llm = ProviderFactory.get_provider(provider, model_id)
            
            # 1. V0 Execution (Baseline)
            status.write("🧠 Generando V0 (Baseline)...")
            start_v0 = time.time()
            resp_v0 = llm.invoke(prompt).content
            time_v0 = time.time() - start_v0
            
            # 2. V1 Execution (RAG)
            status.write("📚 Buscando documentos (RAG)...")
            retrieved_docs = rag_engine.retrieve_context(prompt)
            
            status.write("🧠 Generando V1 (RAG Augmented)...")
            start_v1 = time.time()
            rag_chain = rag_engine.get_chain(llm)
            resp_v1 = rag_chain.invoke(prompt)
            time_v1 = time.time() - start_v1
            
            status.update(label="¡Completado!", state="complete", expanded=False)
            
            # Render Comparison with Scrollable Containers
            st.markdown("### ⚖️ Resultados de Comparativa")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"#### V0 (Sin RAG) - Baseline")
                st.caption(f"⏱️ Tiempo: {time_v0:.2f}s")
                # Scrollable container for V0
                st.markdown(
                    f"""
                    <div style="height: 400px; overflow-y: auto; background-color: #262730; padding: 15px; border-radius: 5px; border: 1px solid #4a4a4a;">
                        {resp_v0}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(f"#### V1 (Con RAG) - Aumentado")
                st.caption(f"⏱️ Tiempo: {time_v1:.2f}s")
                # Scrollable container for V1
                st.markdown(
                    f"""
                    <div style="height: 400px; overflow-y: auto; background-color: #1e1e1e; padding: 15px; border-radius: 5px; border: 1px solid #4a4a4a;">
                        {resp_v1}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # Sources specifically for V1
                st.divider()
                st.markdown("**📄 Fuentes utilizadas (RAG V1):**")
                st.caption(f"Documentos recuperados: {len(retrieved_docs)}")
                for i, doc in enumerate(retrieved_docs):
                    with st.expander(f"Fuente {i+1}: {doc.metadata.get('title', 'Unknown')}"):
                        st.caption(f"ID: {doc.metadata.get('source_id')}")
                        st.markdown(f"*{doc.page_content[:400]}...*")

            # Save to history
            st.session_state.messages.append({
                "role": "assistant",
                "model": model_id,
                "v0": resp_v0,
                "time_v0": time_v0,
                "v1": resp_v1,
                "time_v1": time_v1,
                "sources": retrieved_docs
            })
            
        except Exception as e:
            st.error(f"Error: {e}")
