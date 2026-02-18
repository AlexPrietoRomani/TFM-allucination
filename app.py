import streamlit as st
import json
import time
import asyncio
from pathlib import Path

# --- Imports ---
from src.core.providers.factory import ProviderFactory
from src.core.config.settings import settings
from src.chat.rag import RAGEngine
from src.agent.graph import AgentGraph
from langchain_core.messages import HumanMessage, AIMessage
import pandas as pd

# Eval Imports
try:
    from eval.run_eval import evaluate_row_v0_v1
    from eval.run_eval_v2 import evaluate_row_v2
    from reports.generate_report import generate_report
except ImportError:
    pass

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
    
    # Mode Selection
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

# --- Helper Functions ---

def render_metrics(metrics_data):
    """Renderiza las métricas de calidad con descripciones."""
    if not metrics_data: return
    
    with st.expander("📊 Métricas de Calidad", expanded=True):
        mc1, mc2, mc3 = st.columns(3)
        
        faith_score = metrics_data.get('faith_score', 0)
        rel_score = metrics_data.get('rel_score', 0)
        fs_score = metrics_data.get('factscore', 0)
        
        with mc1:
            st.metric("⚖️ Fidelidad", f"{faith_score:.2f}")
            st.caption("_Mide si la respuesta se deriva exclusivamente del contexto, sin inventar datos._")
        with mc2:
            st.metric("🎯 Relevancia", f"{rel_score:.2f}")
            st.caption("_Mide si los documentos recuperados contienen la información necesaria._")
        with mc3:
            st.metric("🔬 FactScore", f"{fs_score:.2f}")
            st.caption("_Descompone la respuesta en hechos atómicos y verifica cada uno._")
        
        # Razones
        faith_reason = metrics_data.get('faith_reason', '')
        rel_reason = metrics_data.get('rel_reason', '')
        if faith_reason:
            st.info(f"**Fidelidad:** {faith_reason}")
        if rel_reason:
            st.info(f"**Relevancia:** {rel_reason}")
        
        # Desglose FactScore
        if "fs_breakdown" in metrics_data and metrics_data["fs_breakdown"]:
            st.markdown("---")
            st.markdown(f"**Desglose FactScore** ({metrics_data.get('supported_claims', 0)}/{metrics_data.get('total_claims', 0)} soportados)")
            for item in metrics_data["fs_breakdown"]:
                label = item.get('label', 'NoVerificado')
                if label == 'Soportado':
                    st.markdown(f"✅ {item['claim']}")
                elif label == 'Contradicho':
                    st.markdown(f"❌ {item['claim']} — _{item.get('reason', '')}_")
                else:
                    st.markdown(f"⚠️ {item['claim']} — _{item.get('reason', '')}_")


def calculate_metrics_sync(prompt, response, retrieved_docs, status_container=None):
    """Calcula las 3 métricas de forma síncrona: Fidelidad, Relevancia, FactScore."""
    metrics = {}
    if not use_metrics or not FaithfulnessMetric:
        return metrics
    
    try:
        if status_container:
            status_container.write("⚖️ Calculando Fidelidad...")
        faith_metric = FaithfulnessMetric()
        faith_res = faith_metric.evaluate(response, retrieved_docs)
        
        if status_container:
            status_container.write("🎯 Calculando Relevancia...")
        rel_metric = ContextRelevanceMetric()
        rel_res = rel_metric.evaluate(prompt, retrieved_docs)
        
        metrics = {
            "faith_score": faith_res.get("score", 0.0),
            "faith_reason": faith_res.get("reason", "N/A"),
            "rel_score": rel_res.get("score", 0.0),
            "rel_reason": rel_res.get("reason", "N/A"),
        }
        
        # FactScore (síncrono)
        if FactScoreMetric and retrieved_docs:
            if status_container:
                status_container.write("� Calculando FactScore (puede tardar)...")
            try:
                fs_metric = FactScoreMetric()
                fs_res = fs_metric.calculate(response, retrieved_docs)
                metrics["factscore"] = fs_res.get("score", 0.0)
                metrics["total_claims"] = fs_res.get("total_claims", 0)
                metrics["supported_claims"] = fs_res.get("supported_claims", 0)
                metrics["fs_breakdown"] = fs_res.get("breakdown", [])
            except Exception as e:
                print(f"Error FactScore: {e}")
                metrics["factscore"] = 0.0
                metrics["fs_breakdown"] = []
                
    except Exception as e:
        st.error(f"Error métricas: {e}")
    return metrics


async def run_agent_v2(agent_instance, prompt, status_box):
    """Ejecuta el agente V2 y captura pasos + documentos."""
    log = []
    final_resp = ""
    docs = []
    
    async for event in agent_instance.app.astream_events({"question": prompt}, version="v1"):
        kind = event["event"]
        name = event["name"]
        
        if kind == "on_chain_start" and name in ["retrieve", "generate", "grade", "classify", "chitchat"]:
            status_box.write(f"▶️ V2 Nodo: **{name}**")
            log.append(f"Start: {name}")
            
        if kind == "on_chain_end" and name == "retrieve":
             data = event["data"].get("output")
             if data and "documents" in data:
                 docs = data["documents"]

    final_state = await agent_instance.app.ainvoke({"question": prompt})
    final_resp = final_state.get("generation", "")
    return final_resp, docs, log


def run_model_a(mode_label, prompt, llm, status):
    """Ejecuta el lado A de la comparación."""
    if mode_label == "V0":
        t0 = time.time()
        resp = llm.invoke(prompt).content
        return "V0 (Baseline)", resp, time.time() - t0, [], {}
    elif mode_label == "V1":
        t0 = time.time()
        docs = rag_engine.retrieve_context(prompt)
        resp = rag_engine.get_chain(llm).invoke(prompt)
        met = calculate_metrics_sync(prompt, resp, docs, status)
        return "V1 (RAG)", resp, time.time() - t0, docs, met
    elif mode_label == "V2":
        t0 = time.time()
        agent = get_agent_v2(provider, model_id)
        resp, docs, steps = asyncio.run(run_agent_v2(agent, prompt, status))
        met = calculate_metrics_sync(prompt, resp, docs, status)
        return "V2 (Agente)", resp, time.time() - t0, docs, met


# --- Main Tabs ---
st.title("🍇 Plataforma TFM: Arándanos AI")

tab_comp, tab_v0, tab_v1, tab_v2, tab_reports = st.tabs([
    "⚔️ Comparativa", "🧠 V0 (Baseline)", "📚 V1 (RAG)", "🤖 V2 (Agente)", "📊 Reportes & Eval"
])

# ═══════════════════════════════════════════════════════════════════════════
# TAB V0 (Baseline)
# ═══════════════════════════════════════════════════════════════════════════
with tab_v0:
    st.subheader("Chat V0: Modelo Base (Sin Contexto)")
    st.caption("_El LLM responde directamente sin acceso a documentos. Útil como línea base para medir mejoras._")
    
    for msg in st.session_state.messages_v0:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "time" in msg: st.caption(f"⏱️ {msg['time']:.2f}s")

    if prompt_v0 := st.chat_input("Pregunta a V0...", key="input_v0"):
        st.session_state.messages_v0.append({"role": "user", "content": prompt_v0})
        st.rerun()

if st.session_state.messages_v0 and st.session_state.messages_v0[-1]["role"] == "user":
    with tab_v0:
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
                st.caption(f"⏱️ {dt:.2f}s")
                st.session_state.messages_v0.append({"role": "assistant", "content": resp, "time": dt})
            except Exception as e:
                st.error(f"Error: {e}")

# ═══════════════════════════════════════════════════════════════════════════
# TAB V1 (RAG)
# ═══════════════════════════════════════════════════════════════════════════
with tab_v1:
    st.subheader("Chat V1: RAG Estándar (Retrieval-Augmented)")
    st.caption("_El sistema busca documentos relevantes en Qdrant antes de generar la respuesta, reduciendo alucinaciones._")
    
    for msg in st.session_state.messages_v1:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "time" in msg: st.caption(f"⏱️ {msg['time']:.2f}s")
            if "metrics" in msg: render_metrics(msg["metrics"])
            if "sources" in msg:
                with st.expander(f"📄 Fuentes ({len(msg['sources'])})"):
                    for d in msg['sources']:
                        st.caption(f"- {d.metadata.get('title','Doc')} ({d.metadata.get('source_id', '')})")

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
                
                # Metrics (Fidelidad + Relevancia + FactScore)
                met = calculate_metrics_sync(prompt, resp, docs, status)
                
                dt = time.time() - t0
                status.update(label="Listo", state="complete")
                
                st.markdown(resp)
                st.caption(f"⏱️ {dt:.2f}s")
                render_metrics(met)
                
                with st.expander(f"📄 Fuentes ({len(docs)})"):
                    for d in docs:
                        st.caption(f"- {d.metadata.get('title','Doc')} ({d.metadata.get('source_id', '')})")
                
                st.session_state.messages_v1.append({
                    "role": "assistant", "content": resp, "time": dt,
                    "metrics": met, "sources": docs
                })
            except Exception as e:
                 st.error(f"Error: {e}")

# ═══════════════════════════════════════════════════════════════════════════
# TAB V2 (Agent)
# ═══════════════════════════════════════════════════════════════════════════
with tab_v2:
    st.subheader("Chat V2: Agente Autónomo (LangGraph)")
    st.caption("_Agente con ciclos de auto-corrección: si detecta una alucinación, reescribe la respuesta automáticamente._")
    
    for msg in st.session_state.messages_v2:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "time" in msg: st.caption(f"⏱️ {msg['time']:.2f}s")
            if "metrics" in msg: render_metrics(msg["metrics"])
            if "steps" in msg: 
                with st.expander("🔍 Trazabilidad (Pasos del Agente)"):
                    st.json(msg["steps"])

    if prompt_v2 := st.chat_input("Pregunta a V2...", key="input_v2"):
        st.session_state.messages_v2.append({"role": "user", "content": prompt_v2})
        st.rerun()

if st.session_state.messages_v2 and st.session_state.messages_v2[-1]["role"] == "user":
    with tab_v2:
        prompt = st.session_state.messages_v2[-1]["content"]
        with st.chat_message("assistant"):
            status = st.status("Agente V2 Pensando...")
            t0 = time.time()
            try:
                current_agent = get_agent_v2(provider, model_id)
                resp, docs, steps = asyncio.run(run_agent_v2(current_agent, prompt, status))
                
                # Metrics (Fidelidad + Relevancia + FactScore)
                met = calculate_metrics_sync(prompt, resp, docs, status)
                
                dt = time.time() - t0
                status.update(label="Listo", state="complete")
                st.markdown(resp)
                st.caption(f"⏱️ {dt:.2f}s")
                render_metrics(met)
                
                with st.expander("🔍 Trazabilidad (Pasos del Agente)"):
                    st.json(steps)
                
                st.session_state.messages_v2.append({
                    "role": "assistant", "content": resp, "time": dt,
                    "metrics": met, "steps": steps
                })
            except Exception as e:
                st.error(f"Error V2: {e}")

# ═══════════════════════════════════════════════════════════════════════════
# TAB COMPARATIVA
# ═══════════════════════════════════════════════════════════════════════════
with tab_comp:
    st.subheader(f"⚔️ Comparativa: {compare_mode}")
    
    if compare_mode == "V0 vs V1 vs V2":
        st.caption("_Ejecuta las tres versiones simultáneamente para la misma pregunta._")
    else:
        st.caption(f"_Compara las respuestas de {compare_mode} lado a lado con métricas de calidad._")
    
    # --- Render History ---
    for msg in st.session_state.messages_comp:
        if msg["role"] == "user":
            with st.chat_message("user"): st.markdown(msg["content"])
        else:
            with st.chat_message("assistant"):
                is_triple = msg.get("mode") == "V0 vs V1 vs V2"
                
                if is_triple:
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        st.markdown(f"**{msg['model_a_name']}**")
                        st.caption(f"⏱️ {msg['time_a']:.2f}s")
                        st.info(msg['resp_a'])
                        if msg.get('metrics_a'): render_metrics(msg['metrics_a'])
                    with c2:
                        st.markdown(f"**{msg['model_b_name']}**")
                        st.caption(f"⏱️ {msg['time_b']:.2f}s")
                        st.success(msg['resp_b'])
                        if msg.get('metrics_b'): render_metrics(msg['metrics_b'])
                    with c3:
                        st.markdown(f"**{msg['model_c_name']}**")
                        st.caption(f"⏱️ {msg['time_c']:.2f}s")
                        st.warning(msg['resp_c'])
                        if msg.get('metrics_c'): render_metrics(msg['metrics_c'])
                else:
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown(f"**{msg['model_a_name']}**")
                        st.caption(f"⏱️ {msg['time_a']:.2f}s")
                        st.info(msg['resp_a'])
                        if msg.get('metrics_a'): render_metrics(msg['metrics_a'])
                    with c2:
                        st.markdown(f"**{msg['model_b_name']}**")
                        st.caption(f"⏱️ {msg['time_b']:.2f}s")
                        st.success(msg['resp_b'])
                        if msg.get('metrics_b'): render_metrics(msg['metrics_b'])

    if prompt_comp := st.chat_input("Comparar modelos...", key="input_comp"):
        st.session_state.messages_comp.append({"role": "user", "content": prompt_comp})
        st.rerun()

if st.session_state.messages_comp and st.session_state.messages_comp[-1]["role"] == "user":
    with tab_comp:
        prompt = st.session_state.messages_comp[-1]["content"]
        with st.chat_message("assistant"):
            status = st.status(f"Ejecutando {compare_mode}...")
            
            try:
                llm = ProviderFactory.get_provider(provider, model_id)
                
                if compare_mode == "V0 vs V1 vs V2":
                    # ═══ TRIPLE COMPARISON ═══
                    status.write("🧠 Ejecutando V0 (Baseline)...")
                    t0 = time.time()
                    resp_v0 = llm.invoke(prompt).content
                    time_v0 = time.time() - t0
                    
                    status.write("📚 Ejecutando V1 (RAG)...")
                    t0 = time.time()
                    docs_v1 = rag_engine.retrieve_context(prompt)
                    resp_v1 = rag_engine.get_chain(llm).invoke(prompt)
                    met_v1 = calculate_metrics_sync(prompt, resp_v1, docs_v1, status)
                    time_v1 = time.time() - t0
                    
                    status.write("🤖 Ejecutando V2 (Agente)...")
                    t0 = time.time()
                    agent = get_agent_v2(provider, model_id)
                    resp_v2, docs_v2, steps_v2 = asyncio.run(run_agent_v2(agent, prompt, status))
                    met_v2 = calculate_metrics_sync(prompt, resp_v2, docs_v2, status)
                    time_v2 = time.time() - t0
                    
                    status.update(label="Comparación Triple Completada", state="complete")
                    
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        st.markdown("**V0 (Baseline)**")
                        st.caption(f"⏱️ {time_v0:.2f}s")
                        st.info(resp_v0)
                    with c2:
                        st.markdown("**V1 (RAG)**")
                        st.caption(f"⏱️ {time_v1:.2f}s")
                        st.success(resp_v1)
                        render_metrics(met_v1)
                    with c3:
                        st.markdown("**V2 (Agente)**")
                        st.caption(f"⏱️ {time_v2:.2f}s")
                        st.warning(resp_v2)
                        render_metrics(met_v2)
                    
                    st.session_state.messages_comp.append({
                        "role": "assistant",
                        "model_a_name": "V0 (Baseline)", "resp_a": resp_v0, "time_a": time_v0, "metrics_a": {},
                        "model_b_name": "V1 (RAG)", "resp_b": resp_v1, "time_b": time_v1, "metrics_b": met_v1,
                        "model_c_name": "V2 (Agente)", "resp_c": resp_v2, "time_c": time_v2, "metrics_c": met_v2,
                        "mode": compare_mode
                    })
                    
                else:
                    # ═══ DUAL COMPARISON ═══
                    parts = compare_mode.split(" vs ")
                    
                    # Run side A
                    name_a, resp_a, time_a, docs_a, met_a = run_model_a(parts[0], prompt, llm, status)
                    
                    # Run side B
                    name_b, resp_b, time_b, docs_b, met_b = run_model_a(parts[1], prompt, llm, status)
                    
                    status.update(label="Comparación Completada", state="complete")
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown(f"**{name_a}**")
                        st.caption(f"⏱️ {time_a:.2f}s")
                        st.info(resp_a)
                        render_metrics(met_a)
                    with c2:
                        st.markdown(f"**{name_b}**")
                        st.caption(f"⏱️ {time_b:.2f}s")
                        st.success(resp_b)
                        render_metrics(met_b)
                    
                    st.session_state.messages_comp.append({
                        "role": "assistant",
                        "model_a_name": name_a, "resp_a": resp_a, "time_a": time_a, "metrics_a": met_a,
                        "model_b_name": name_b, "resp_b": resp_b, "time_b": time_b, "metrics_b": met_b,
                        "mode": compare_mode
                    })
                    
            except Exception as e:
                st.error(f"Error Comparativa: {e}")

# ═══════════════════════════════════════════════════════════════════════════
# TAB REPORTES
# ═══════════════════════════════════════════════════════════════════════════
with tab_reports:
    st.subheader("📊 Centro de Control de Evaluación")
    
    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.markdown("### Configuración")
        q_bank_path = st.text_input("Banco de Preguntas", value="eval/question_bank_v1.csv")
        limit_q = st.slider("Límite de Preguntas", 1, 20, 5)
        
        st.markdown("#### Versiones a Evaluar")
        run_v0_v1 = st.checkbox("Ejecutar V0 (Base) y V1 (RAG)", value=True)
        run_v2_eval = st.checkbox("Ejecutar V2 (Agente)", value=True)
        
        st.info(f"Proveedor Activo: **{provider}**\nModelo: **{model_id}**")
        
        if st.button("🚀 Iniciar Benchmark", type="primary"):
            if not Path(q_bank_path).exists():
                st.error("No se encuentra el archivo de preguntas.")
            else:
                st.session_state['run_eval'] = True
    
    with c2:
        st.markdown("### Progreso en Tiempo Real")
        status_container = st.container()
        progress_bar = st.progress(0)
        log_area = st.empty()
        
        if st.session_state.get('run_eval', False):
            st.session_state['run_eval'] = False
            
            try:
                df_q = pd.read_csv(q_bank_path, dtype={'id': str})
                if limit_q > 0:
                    df_q = df_q.head(limit_q)
                
                total_steps = len(df_q)
                results_v0_v1 = []
                results_v2 = []
                
                llm = ProviderFactory.get_provider(provider, model_id)
                rag_engine_inst = get_rag_engine()
                rag_chain = rag_engine_inst.get_chain(llm)
                
                agent_instance = None
                if run_v2_eval:
                    agent_instance = get_agent_v2(provider, model_id)
                
                for i, row in df_q.iterrows():
                    q_id = row.get('id', str(i))
                    q_text = row.get('question', '')
                    
                    status_container.markdown(f"**Procesando Q{q_id}:** _{q_text}_")
                    
                    if run_v0_v1:
                        log_area.text(f"Evaluando V0/V1 para Q{q_id}...")
                        res_1 = evaluate_row_v0_v1(row, llm, rag_chain, provider, model_id, run_label="ui_run")
                        results_v0_v1.append(res_1)
                    
                    if run_v2_eval and agent_instance:
                        log_area.text(f"Evaluando V2 (Agente) para Q{q_id}...")
                        res_2 = asyncio.run(evaluate_row_v2(row, agent_instance))
                        results_v2.append(res_2)
                    
                    progress_bar.progress((i + 1) / total_steps)
                
                st.success("✅ Evaluación Completada")
                
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                
                if results_v0_v1:
                    df_1 = pd.DataFrame(results_v0_v1)
                    path_1 = Path(f"eval/results/Comparison/eval_comparison_{provider}_{timestamp}.csv")
                    path_1.parent.mkdir(parents=True, exist_ok=True)
                    df_1.to_csv(path_1, index=False)
                    st.toast(f"Resultados V0/V1 guardados en {path_1.name}")

                if results_v2:
                    path_2 = Path(f"eval/results/V2/eval_v2_{timestamp}.json")
                    path_2.parent.mkdir(parents=True, exist_ok=True)
                    with open(path_2, "w", encoding="utf-8") as f:
                        json.dump(results_v2, f, indent=2, ensure_ascii=False)
                    st.toast(f"Resultados V2 guardados en {path_2.name}")
                
            except Exception as e:
                st.error(f"Error durante evaluación: {e}")

    st.divider()
    
    st.subheader("📄 Generación de Reportes")
    c_rep1, c_rep2 = st.columns(2)
    with c_rep1:
        rep_mode = st.selectbox("Versión del Reporte", ["all", "v0", "v1", "v2"])
        if st.button("Generar Informe Final Markdown"):
            try:
                out_path = generate_report(rep_mode)
                if out_path:
                    st.success(f"Reporte generado: {out_path}")
                    with open(out_path, "rb") as f:
                        st.download_button("⬇️ Descargar Reporte (.md)", f, file_name=Path(out_path).name)
            except Exception as e:
                st.error(f"Error generando reporte: {e}")
