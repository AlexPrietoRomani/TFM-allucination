import streamlit as st
import json
from pathlib import Path

# --- Imports Core ---
from src.core.config.settings import settings
from src.chat.rag import RAGEngine
from src.agent.graph import AgentGraph

# --- Imports UI Modules ---
from src.ui.tabs.tab_v0 import render_tab_v0
from src.ui.tabs.tab_v1 import render_tab_v1
from src.ui.tabs.tab_v2 import render_tab_v2
from src.ui.tabs.tab_comparison import render_tab_comparison
from src.ui.tabs.tab_reports import render_tab_reports

# --- Page Config ---
st.set_page_config(
    page_title="TFM Chatbot (Unificado)",
    page_icon="🫐",
    layout="wide"
)

# --- Initialization & Caching ---

REGISTRY_PATH = Path("src/core/config/model_registry.json")

@st.cache_data
def load_model_registry():
    if not REGISTRY_PATH.exists():
        return {}
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@st.cache_resource
def get_rag_engine():
    return RAGEngine()

@st.cache_resource
def get_agent_v2(provider_name=None, model_name=None):
    return AgentGraph(provider=provider_name, model_id=model_name)

registry = load_model_registry()
rag_engine = get_rag_engine()

# --- Session State ---
if "messages_v0" not in st.session_state: st.session_state.messages_v0 = []
if "messages_v1" not in st.session_state: st.session_state.messages_v1 = []
if "messages_v2" not in st.session_state: st.session_state.messages_v2 = []
if "messages_comp" not in st.session_state: st.session_state.messages_comp = []

# --- Sidebar Configuration ---
with st.sidebar:
    st.header("⚙️ Configuración Global")
    
    # Provider Selection
    providers = ["gemini", "openrouter", "ollama"]
    provider = st.selectbox("Proveedor LLM", providers, index=0)
    
    if provider == "ollama":
        model_id = st.text_input("Modelo", value=settings.default_ollama_model, help="Nombre exacto del modelo Ollama (ej: qwen2.5:3b)")
    else:
        available_models = [m["id"] for m in registry.get("providers", {}).get(provider, [])]
        default_model = settings.default_model_google if provider == "gemini" else settings.default_model_openrouter
        try:
            def_index = available_models.index(default_model)
        except ValueError:
            def_index = 0
        model_id = st.selectbox("Modelo", available_models, index=def_index)
        
    st.divider()
    
    # Mode Selection (Para la pestaña Comparativa)
    st.write("🔧 **Opciones de Comparativa**")
    compare_mode = st.selectbox(
        "Modo Comparación",
        ["V0 vs V1", "V1 vs V2", "V0 vs V2", "V0 vs V1 vs V2"],
        index=0
    )
    
    use_metrics = st.checkbox("📊 Calcular Métricas", value=False, help="Evalúa Fidelidad, Relevancia y FactScore en V1/V2")

    st.divider()
    if st.button("🗑️ Limpiar Todos los Historiales"):
        st.session_state.messages_v0 = []
        st.session_state.messages_v1 = []
        st.session_state.messages_v2 = []
        st.session_state.messages_comp = []
        st.rerun()

# --- Main Tabs Orchestration ---
st.title("🍇 Plataforma TFM: Arándanos AI")

# Definir pestañas
tab_comp, tab_v0, tab_v1, tab_v2, tab_reports = st.tabs([
    "⚔️ Comparativa", "🧠 V0 (Baseline)", "📚 V1 (RAG)", "🤖 V2 (Agente)", "📊 Reportes & Eval"
])

# Obtener instancia del agente para reutilizar en pestañas relevantes
current_agent = get_agent_v2(provider, model_id)

# Renderizar Pestaña Comparativa
with tab_comp:
    render_tab_comparison(provider, model_id, rag_engine, current_agent, compare_mode, use_metrics)

# Renderizar Pestaña V0
with tab_v0:
    render_tab_v0(provider, model_id)

# Renderizar Pestaña V1
with tab_v1:
    render_tab_v1(rag_engine, provider, model_id, use_metrics)

# Renderizar Pestaña V2
with tab_v2:
    render_tab_v2(current_agent, provider, model_id, use_metrics)

# Renderizar Pestaña Reportes
with tab_reports:
    render_tab_reports(provider, model_id, rag_engine, current_agent)
