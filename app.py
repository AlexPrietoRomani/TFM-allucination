import streamlit as st
import json
import time
import asyncio
from pathlib import Path

# --- Imports (Lazy loaded components imported only when needed if possible, or centrally here) ---
from src.core.providers.factory import ProviderFactory
from src.core.config.settings import settings
from src.chat.rag import RAGEngine
from src.agent.graph import AgentGraph
from langchain_core.messages import HumanMessage, AIMessage

# Import Metrics
try:
    from src.metrics.faithfulness import FaithfulnessMetric
    from src.metrics.context_relevance import ContextRelevanceMetric
    from src.metrics.factscore import FactScoreMetric
except ImportError:
    FaithfulnessMetric = None
    ContextRelevanceMetric = None
    FactScoreMetric = None

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
def get_agent_v2():
    return AgentGraph()

registry = load_model_registry()
rag_engine = get_rag_engine()
agent_v2 = get_agent_v2()

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
        model_id = st.text_input("Modelo", value="gpt-oss:20b", help="Nombre exacto del modelo Ollama")
    else:
        available_models = [m["id"] for m in registry.get("providers", {}).get(provider, [])]
        default_model = settings.default_model_google if provider == "gemini" else settings.default_model_openrouter
        try:
            def_index = available_models.index(default_model)
        except ValueError:
            def_index = 0
        model_id = st.selectbox("Modelo", available_models, index=def_index)
        
    st.divider()
    
    # Mode Selection (Though we use Tabs, this affects Comparer)
    st.write("🔧 **Opciones de Comparativa**")
    compare_mode = st.selectbox("Modo Comparación", ["V0 vs V1", "V1 vs V2", "V0 vs V2"], index=0)
    
    use_metrics = st.checkbox("📊 Calcular Métricas (Lento)", value=False, help="Evalúa Fidelidad/Relevancia/FactScore en V1/V2")

    st.divider()
    if st.button("🗑️ Limpiar Todos los Historiales"):
        st.session_state.messages_v0 = []
        st.session_state.messages_v1 = []
        st.session_state.messages_v2 = []
        st.session_state.messages_comp = []
        st.rerun()

# --- Helper Functions ---

# Redis Connection (Lazy)
def get_redis_queue():
    try:
        from redis import Redis
        from rq import Queue
        r = Redis(host="localhost", port=6379, socket_connect_timeout=1)
        # Check connection
        r.ping()
        return Queue(connection=r)
    except Exception as e:
        print(f"Redis not available: {e}")
        return None

def submit_async_metric(response, docs):
    q = get_redis_queue()
    if not q: return None
    
    # Serialize docs
    docs_data = [{"page_content": d.page_content, "metadata": d.metadata} for d in docs]
    
    try:
        job = q.enqueue('services.worker.tasks.calculate_factscore_task', response, docs_data, result_ttl=3600)
        return job.id
    except Exception as e:
        print(f"Job submit failed: {e}")
        return None

def check_async_job(job_id):
    if not job_id: return None
    try:
        from redis import Redis
        from rq.job import Job
        r = Redis(host="localhost", port=6379)
        job = Job.fetch(job_id, connection=r)
        if job.is_finished:
            return job.result
        return None
    except:
        return None

def render_metrics(metrics_data):
    if not metrics_data: return
    
    with st.expander("📊 Métricas de Calidad"):
        # Check if we have async job pending
        if "job_id" in metrics_data and "factscore" not in metrics_data:
            job_id = metrics_data["job_id"]
            res = check_async_job(job_id)
            if res:
                metrics_data["factscore"] = res.get("score", 0.0)
                metrics_data["fs_breakdown"] = res.get("breakdown", [])
                st.toast("¡Cálculo FactScore completado!")
            else:
                st.caption("⏳ Calculando FactScore en background...")
                if st.button("🔄 Actualizar Status", key=f"btn_{job_id}"):
                    st.rerun()

        mc1, mc2, mc3 = st.columns(3)
        mc1.metric("Fidelidad", f"{metrics_data.get('faith_score', 0):.2f}")
        mc2.metric("Relevancia", f"{metrics_data.get('rel_score', 0):.2f}")
        
        fs_display = f"{metrics_data.get('factscore', 0):.2f}" if "factscore" in metrics_data else "..."
        mc3.metric("FactScore", fs_display)
        
        st.caption(f"Reason: {metrics_data.get('faith_reason', 'N/A')}")
        
        if "fs_breakdown" in metrics_data and metrics_data["fs_breakdown"]:
            st.markdown("---")
            st.markdown("**Desglose FactScore:**")
            for item in metrics_data["fs_breakdown"]:
                icon = "✅" if item['label'] == 'Soportado' else "❌"
                st.markdown(f"{icon} {item['claim']}")

def calculate_metrics_sync(prompt, response, retrieved_docs, status_container):
    metrics = {}
    if use_metrics and FaithfulnessMetric:
        # Launch Async if possible for FactScore
        # Calculate fast metrics here
        status_container.write("⚖️ Calculando Métricas Rápidas (Fidelidad)...")
        try:
            faith_metric = FaithfulnessMetric()
            rel_metric = ContextRelevanceMetric()
            
            # Relevance
            rel_res = rel_metric.evaluate(prompt, retrieved_docs)
            # Faithfulness
            faith_res = faith_metric.evaluate(response, retrieved_docs)
            
            metrics = {
                "faith_score": faith_res.get("score", 0.0),
                "faith_reason": faith_res.get("reason", "N/A"),
                "rel_score": rel_res.get("score", 0.0),
                "rel_reason": rel_res.get("reason", "N/A")
            }
            
            # Async FactScore
            status_container.write("🚀 Enviando FactScore a Worker...")
            jid = submit_async_metric(response, retrieved_docs)
            if jid:
                metrics["job_id"] = jid
                status_container.write(f"✅ Job enviado: {jid}")
            else:
                 # Fallback Sync
                 pass
                 
        except Exception as e:
            st.error(f"Error métricas: {e}")
    return metrics

async def run_agent_v2(prompt, status_box):
    log = []
    final_resp = ""
    docs = []
    
    # Listen to events
    async for event in agent_v2.app.astream_events({"question": prompt}, version="v1"):
        kind = event["event"]
        name = event["name"]
        
        if kind == "on_chain_start" and name in ["retrieve", "generate", "grade", "classify", "chitchat"]:
            status_box.write(f"▶️ V2 Nodo: **{name}**")
            log.append(f"Start: {name}")
            
        if kind == "on_chain_end" and name == "retrieve":
             # Try capture docs
             data = event["data"].get("output")
             if data and "documents" in data:
                 docs = data["documents"]

    # Final result
    final_state = await agent_v2.app.ainvoke({"question": prompt})
    final_resp = final_state.get("generation", "")
    return final_resp, docs, log

# --- Main Tabs ---
st.title("🍇 Plataforma TFM: Arándanos AI")

tab_comp, tab_v0, tab_v1, tab_v2 = st.tabs(["⚔️ Comparativa", "🧠 V0 (Baseline)", "📚 V1 (RAG)", "🤖 V2 (Agente)"])

# === TAB V0 (Baseline) ===
with tab_v0:
    st.subheader("Chat V0: Modelo Base (Sin Contexto)")
    for msg in st.session_state.messages_v0:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "time" in msg: st.caption(f"⏱️ {msg['time']:.2f}s")

    if prompt_v0 := st.chat_input("Pregunta a V0...", key="input_v0"):
        st.session_state.messages_v0.append({"role": "user", "content": prompt_v0})
        st.rerun() # Rerun to show user msg immediately

if st.session_state.messages_v0 and st.session_state.messages_v0[-1]["role"] == "user":
    with tab_v0: # Context manager again for the generation part after rerun logic
        prompt = st.session_state.messages_v0[-1]["content"]
        with st.chat_message("assistant"):
            status = st.status("Generando V0...")
            t0 = time.time()
            try:
                llm = ProviderFactory.get_provider(provider, model_id)
                resp = llm.invoke(prompt).content
                dt = time.time() - t0
                status.update(label="Listo", state="complete")
                st.markdown(resp)
                st.session_state.messages_v0.append({"role": "assistant", "content": resp, "time": dt})
            except Exception as e:
                st.error(f"Error: {e}")

# === TAB V1 (RAG) ===
with tab_v1:
    st.subheader("Chat V1: RAG Estándar (Retrieval-Augmented)")
    for msg in st.session_state.messages_v1:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "metrics" in msg: render_metrics(msg["metrics"])
            if "sources" in msg:
                with st.expander(f"Fuentes ({len(msg['sources'])})"):
                    for d in msg['sources']: st.caption(f"- {d.metadata.get('title','Doc')}")

    if prompt_v1 := st.chat_input("Pregunta a V1...", key="input_v1"):
        st.session_state.messages_v1.append({"role": "user", "content": prompt_v1})
        st.rerun()

if st.session_state.messages_v1 and st.session_state.messages_v1[-1]["role"] == "user":
    with tab_v1:
        prompt = st.session_state.messages_v1[-1]["content"]
        with st.chat_message("assistant"):
            status = st.status("Ejecutando Pipeline RAG...")
            t0 = time.time()
            try:
                llm = ProviderFactory.get_provider(provider, model_id)
                status.write("🔍 Buscando documentos...")
                docs = rag_engine.retrieve_context(prompt)
                
                status.write("📝 Generando respuesta...")
                rag_chain = rag_engine.get_chain(llm)
                resp = rag_chain.invoke(prompt)
                
                # Metrics
                met = calculate_metrics_sync(prompt, resp, docs, status)
                
                dt = time.time() - t0
                status.update(label="Listo", state="complete")
                
                st.markdown(resp)
                render_metrics(met)
                
                st.session_state.messages_v1.append({
                    "role": "assistant", "content": resp, "time": dt,
                    "metrics": met, "sources": docs
                })
            except Exception as e:
                 st.error(f"Error {e}")

# === TAB V2 (Agent) ===
with tab_v2:
    st.subheader("Chat V2: Agente Autónomo (LangGraph)")
    for msg in st.session_state.messages_v2:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "steps" in msg: 
                with st.expander("Trazabilidad"): st.json(msg["steps"])

    if prompt_v2 := st.chat_input("Pregunta a V2...", key="input_v2"):
        st.session_state.messages_v2.append({"role": "user", "content": prompt_v2})
        st.rerun()

if st.session_state.messages_v2 and st.session_state.messages_v2[-1]["role"] == "user":
    with tab_v2:
        prompt = st.session_state.messages_v2[-1]["content"]
        with st.chat_message("assistant"):
            status = st.status("Agente V2 Pensando...")
            try:
                resp, docs, steps = asyncio.run(run_agent_v2(prompt, status))
                status.update(label="Listo", state="complete")
                st.markdown(resp)
                st.session_state.messages_v2.append({
                    "role": "assistant", "content": resp, "steps": steps
                })
            except Exception as e:
                st.error(f"Error V2: {e}")

# === TAB COMPARATIVA ===
with tab_comp:
    st.subheader(f"⚔️ Comparativa: {compare_mode}")
    
    # Render History
    for msg in st.session_state.messages_comp:
        if msg["role"] == "user":
            with st.chat_message("user"): st.markdown(msg["content"])
        else:
            with st.chat_message("assistant"):
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(f"**{msg['model_a_name']}**")
                    st.caption(f"⏱️ {msg['time_a']:.2f}s")
                    st.info(msg['resp_a'])
                    if 'metrics_a' in msg: render_metrics(msg['metrics_a'])
                with c2:
                    st.markdown(f"**{msg['model_b_name']}**")
                    st.caption(f"⏱️ {msg['time_b']:.2f}s")
                    st.success(msg['resp_b'])
                    if 'metrics_b' in msg: render_metrics(msg['metrics_b'])

    if prompt_comp := st.chat_input("Comparar modelos...", key="input_comp"):
        st.session_state.messages_comp.append({"role": "user", "content": prompt_comp})
        st.rerun()

if st.session_state.messages_comp and st.session_state.messages_comp[-1]["role"] == "user":
    with tab_comp:
        prompt = st.session_state.messages_comp[-1]["content"]
        with st.chat_message("assistant"):
            status = st.status(f"Ejecutando {compare_mode}...")
            
            # Identify models A and B based on selection
            # "V0 vs V1", "V1 vs V2", "V0 vs V2"
            try:
                llm = ProviderFactory.get_provider(provider, model_id)
                
                resp_a, resp_b = "", ""
                time_a, time_b = 0, 0
                met_a, met_b = {}, {}
                name_a, name_b = "", ""

                # LOGIC A
                if "V0" in compare_mode.split(" vs ")[0]:
                    name_a = "V0 (Baseline)"
                    t0 = time.time()
                    resp_a = llm.invoke(prompt).content
                    time_a = time.time() - t0
                elif "V1" in compare_mode.split(" vs ")[0]:
                    name_a = "V1 (RAG)"
                    t0 = time.time()
                    docs_a = rag_engine.retrieve_context(prompt)
                    resp_a = rag_engine.get_chain(llm).invoke(prompt)
                    met_a = calculate_metrics_sync(prompt, resp_a, docs_a, status)
                    time_a = time.time() - t0

                # LOGIC B
                if "V1" in compare_mode.split(" vs ")[1] and "V0" in compare_mode.split(" vs ")[0]:
                    name_b = "V1 (RAG)"
                    t0 = time.time()
                    docs_b = rag_engine.retrieve_context(prompt)
                    resp_b = rag_engine.get_chain(llm).invoke(prompt)
                    met_b = calculate_metrics_sync(prompt, resp_b, docs_b, status)
                    time_b = time.time() - t0
                elif "V2" in compare_mode.split(" vs ")[1]:
                    name_b = "V2 (Agente)"
                    t0 = time.time()
                    # V2 Async
                    resp_b, docs_b, steps_b = asyncio.run(run_agent_v2(prompt, status))
                    # V2 usually has self-eval in steps, but we can re-calc external metrics if wanted
                    # Let's rely on internal V2 grading steps for metric or recalc? 
                    # Recalc consistent metrics for comparison
                    met_b = calculate_metrics_sync(prompt, resp_b, docs_b, status)
                    time_b = time.time() - t0
                
                status.update(label="Comparación Completada", state="complete")
                
                # Render results immediately
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(f"**{name_a}**")
                    st.info(resp_a)
                    render_metrics(met_a)
                with c2:
                    st.markdown(f"**{name_b}**")
                    st.success(resp_b)
                    render_metrics(met_b)
                
                # Save
                st.session_state.messages_comp.append({
                    "role": "assistant",
                    "model_a_name": name_a, "resp_a": resp_a, "time_a": time_a, "metrics_a": met_a,
                    "model_b_name": name_b, "resp_b": resp_b, "time_b": time_b, "metrics_b": met_b,
                    "mode": compare_mode
                })
                
            except Exception as e:
                st.error(f"Error Comparativa: {e}")
