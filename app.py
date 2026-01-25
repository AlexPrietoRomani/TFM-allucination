import streamlit as st
import json
import time
import asyncio
from pathlib import Path
from src.core.providers.factory import ProviderFactory
from src.core.config.settings import settings
from src.chat.rag import RAGEngine
from langchain_core.messages import HumanMessage, AIMessage

# Import Metrics (lazy load or safe import)
try:
    from src.metrics.faithfulness import FaithfulnessMetric
    from src.metrics.context_relevance import ContextRelevanceMetric
    from src.metrics.factscore import FactScoreMetric
except ImportError:
    FaithfulnessMetric = None
    ContextRelevanceMetric = None
    FactScoreMetric = None

# Configuración de página
st.set_page_config(
    page_title="TFM Chatbot (V0 vs V1)",
    page_icon="🫐",
    layout="wide"
)

# Cargar Registro
REGISTRY_PATH = Path("src/core/config/model_registry.json")

@st.cache_data
def load_model_registry():
    if not REGISTRY_PATH.exists():
        return {}
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

registry = load_model_registry()

# Inicializar Motor RAG
@st.cache_resource
def get_rag_engine():
    return RAGEngine()

rag_engine = get_rag_engine()

# Estado de Sesión
if "messages" not in st.session_state:
    st.session_state.messages = []

# Barra Lateral (Sidebar)
with st.sidebar:
    st.header("⚙️ Configuración")
    
    # Selector de Proveedor/Modelo
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
    
    # Metrics Toggle
    use_metrics = st.checkbox("📊 Calcular Métricas (Lento)", value=False, help="Evalúa Fidelidad y Relevancia usando un Juez LLM (Ollama/Gemini)")
    
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
                    
                    # Metrics History
                    if "metrics" in msg and msg["metrics"]:
                        with st.expander("📊 Métricas Calculadas"):
                            mc1, mc2, mc3 = st.columns(3)
                            mc1.metric("Fidelidad", f"{msg['metrics'].get('faith_score', 0):.2f}")
                            mc2.metric("Relevancia", f"{msg['metrics'].get('rel_score', 0):.2f}")
                            mc3.metric("FactScore", f"{msg['metrics'].get('factscore', 0):.2f}")
                            
                            st.caption(f"**Fe (Juez)**: {msg['metrics'].get('faith_reason', 'N/A')}")
                            
                            if "fs_breakdown" in msg['metrics']:
                                st.markdown("---")
                                st.markdown("**Desglose FactScore:**")
                                for item in msg['metrics']['fs_breakdown']:
                                    icon = "✅" if item['label'] == 'Soportado' else "❌"
                                    st.markdown(f"{icon} {item['claim']}")
                    
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
            try:
                # Invoke LLM directly
                resp_v0 = llm.invoke(prompt).content
            except Exception as e:
                resp_v0 = f"Error V0: {str(e)}"
            time_v0 = time.time() - start_v0
            
            # 2. V1 Execution (RAG)
            status.write("📚 Buscando documentos (RAG)...")
            retrieved_docs = rag_engine.retrieve_context(prompt)
            
            status.write("🧠 Generando V1 (RAG Aumentado)...")
            start_v1 = time.time()
            try:
                rag_chain = rag_engine.get_chain(llm)
                resp_v1 = rag_chain.invoke(prompt)
            except Exception as e:
                resp_v1 = f"Error V1: {str(e)}"
            time_v1 = time.time() - start_v1
            
            # 3. Metrics Calculation
            metrics_data = {}
            if use_metrics and FaithfulnessMetric:
                status.write("⚖️ Calculando Métricas (Juez LLM)...")
                try:
                    # Instantiate with default judge (Ollama/Gemini defined in judges.py)
                    faith_metric = FaithfulnessMetric()
                    rel_metric = ContextRelevanceMetric()
                    
                    # relevance
                    rel_res = rel_metric.evaluate(prompt, retrieved_docs)
                    # faithfulness
                    print("Evaluando Fidelidad...")
                    faith_res = faith_metric.evaluate(resp_v1, retrieved_docs)
                    
                    metrics_data = {
                        "faith_score": faith_res.get("score", 0.0),
                        "faith_reason": faith_res.get("reason", "N/A"),
                        "rel_score": rel_res.get("score", 0.0),
                        "rel_reason": rel_res.get("reason", "N/A")
                    }
                    
                    # FactScore Check
                    if FactScoreMetric:
                         status.write("🔍 Calculando FactScore (Granularidad Atómica)...")
                         print("Evaluando FactScore...")
                         fact_metric = FactScoreMetric()
                         fs_res = fact_metric.calculate(resp_v1, retrieved_docs)
                         metrics_data["factscore"] = fs_res.get("score", 0.0)
                         metrics_data["fs_breakdown"] = fs_res.get("breakdown", [])
                         
                except Exception as e:
                    st.error(f"Error calculando métricas: {e}")
            
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
                
                # Display Metrics
                if metrics_data:
                    st.divider()
                    st.markdown("##### 📊 Métricas de Alucinación")
                    m_col1, m_col2, m_col3 = st.columns(3)
                    m_col1.metric("Fidelidad", f"{metrics_data.get('faith_score', 0):.2f}", help="¿La respuesta se basa 100% en el contexto?")
                    m_col2.metric("Relevancia", f"{metrics_data.get('rel_score', 0):.2f}", help="¿El contexto recuperado es útil?")
                    
                    fs_val = metrics_data.get('factscore', 0.0)
                    m_col3.metric("FactScore", f"{fs_val:.2f}", help="% de afirmaciones atómicas verificadas")
                    
                    with st.expander("🔍 Detalles del Juez (Fidelidad/Relevancia)"):
                        st.markdown(f"**Fidelidad:** {metrics_data.get('faith_reason', 'N/A')}")
                        st.markdown(f"**Relevancia:** {metrics_data.get('rel_reason', 'N/A')}")
                        
                    if "fs_breakdown" in metrics_data and metrics_data["fs_breakdown"]:
                        with st.expander("atom ⚛️ Desglose FactScore (Hechos Atómicos)"):
                            for item in metrics_data["fs_breakdown"]:
                                icon = "✅" if item['label'] == 'Soportado' else "❌" if item['label'] == 'Contradicho' else "⚠️"
                                st.markdown(f"{icon} **{item['claim']}**")
                                st.caption(f"Razón: {item['reason']}")
                
                # Sources
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
                "sources": retrieved_docs,
                "metrics": metrics_data
            })
            
        except Exception as e:
            st.error(f"Error general: {e}")
