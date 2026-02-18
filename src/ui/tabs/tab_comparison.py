import streamlit as st
import time
import asyncio
from src.core.providers.factory import ProviderFactory
from src.ui.utils import render_metrics, calculate_metrics_sync, run_agent_v2

def run_model_a_comparison(mode_label: str, prompt: str, llm, rag_engine, agent_instance, use_metrics, status):
    """
    Ejecuta el lado A de la comparación (o B) de forma genérica.
    """
    if mode_label == "V0":
        t0 = time.time()
        resp = llm.invoke(prompt).content
        return "V0 (Baseline)", resp, time.time() - t0, [], {}
    
    elif mode_label == "V1":
        t0 = time.time()
        # Retrieve
        docs = rag_engine.retrieve_context(prompt)
        # Generate
        chain = rag_engine.get_chain(llm)
        resp = chain.invoke(prompt)
        # Metrics
        met = calculate_metrics_sync(prompt, resp, docs, use_metrics, status)
        return "V1 (RAG)", resp, time.time() - t0, docs, met
    
    elif mode_label == "V2":
        t0 = time.time()
        # Async Agent execution
        resp, docs, steps = asyncio.run(run_agent_v2(agent_instance, prompt, status))
        # Metrics
        met = calculate_metrics_sync(prompt, resp, docs, use_metrics, status)
        return "V2 (Agente)", resp, time.time() - t0, docs, met
        
    return "Error", "Modo desconocido", 0, [], {}

def render_tab_comparison(provider: str, model_id: str, rag_engine, agent_instance, compare_mode: str, use_metrics: bool):
    """
    Renderiza la pestaña Comparativa.
    Soporta modos duales y triple (V0 vs V1 vs V2).
    """
    st.subheader(f"⚔️ Comparativa: {compare_mode}")
    
    if compare_mode == "V0 vs V1 vs V2":
        st.caption("_Ejecuta las tres versiones simultáneamente para la misma pregunta._")
    else:
        st.caption(f"_Compara las respuestas de {compare_mode} lado a lado con métricas de calidad._")
    
    # --- Historial ---
    for msg in st.session_state.messages_comp:
        if msg["role"] == "user":
            with st.chat_message("user"): st.markdown(msg["content"])
        else:
            with st.chat_message("assistant"):
                is_triple = msg.get("mode") == "V0 vs V1 vs V2"
                
                if is_triple:
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        st.markdown(f"**{msg.get('model_a_name', 'A')}**")
                        st.caption(f"⏱️ {msg.get('time_a', 0):.2f}s")
                        st.info(msg['resp_a'])
                        if msg.get('metrics_a'): render_metrics(msg['metrics_a'])
                    with c2:
                        st.markdown(f"**{msg.get('model_b_name', 'B')}**")
                        st.caption(f"⏱️ {msg.get('time_b', 0):.2f}s")
                        st.success(msg['resp_b'])
                        if msg.get('metrics_b'): render_metrics(msg['metrics_b'])
                    with c3:
                        st.markdown(f"**{msg.get('model_c_name', 'C')}**")
                        st.caption(f"⏱️ {msg.get('time_c', 0):.2f}s")
                        st.warning(msg['resp_c'])
                        if msg.get('metrics_c'): render_metrics(msg['metrics_c'])
                else:
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown(f"**{msg.get('model_a_name','A')}**")
                        st.caption(f"⏱️ {msg.get('time_a',0):.2f}s")
                        st.info(msg['resp_a'])
                        if msg.get('metrics_a'): render_metrics(msg['metrics_a'])
                    with c2:
                        st.markdown(f"**{msg.get('model_b_name','B')}**")
                        st.caption(f"⏱️ {msg.get('time_b',0):.2f}s")
                        st.success(msg['resp_b'])
                        if msg.get('metrics_b'): render_metrics(msg['metrics_b'])


    # --- Input ---
    if prompt_comp := st.chat_input("Comparar modelos...", key="input_comp"):
        st.session_state.messages_comp.append({"role": "user", "content": prompt_comp})
        st.rerun() # Refresh to show user message

    # --- Ejecución ---
    # Si hay mensaje de usuario pendiente al final, ejecutar
    if st.session_state.messages_comp and st.session_state.messages_comp[-1]["role"] == "user":
        prompt = st.session_state.messages_comp[-1]["content"]
        
        with st.chat_message("assistant"):
            status = st.status(f"Ejecutando {compare_mode}...")
            
            try:
                llm = ProviderFactory.get_provider(provider, model_id)
                
                if compare_mode == "V0 vs V1 vs V2":
                    # ═══ TRIPLE COMPARISON ═══
                    
                    # 1. V0
                    status.write("🧠 Ejecutando V0 (Baseline)...")
                    n_v0, r_v0, t_v0, _, m_v0 = run_model_a_comparison("V0", prompt, llm, rag_engine, agent_instance, False, status) # V0 NO TIENE metricas (sin contexto)
                    
                    # 2. V1
                    status.write("📚 Ejecutando V1 (RAG)...")
                    n_v1, r_v1, t_v1, _, m_v1 = run_model_a_comparison("V1", prompt, llm, rag_engine, agent_instance, use_metrics, status)
                    
                    # 3. V2
                    status.write("🤖 Ejecutando V2 (Agente)...")
                    n_v2, r_v2, t_v2, d_v2, m_v2 = run_model_a_comparison("V2", prompt, llm, rag_engine, agent_instance, use_metrics, status)
                    
                    # Warning for empty docs in V2
                    if not d_v2:
                         status.warning("⚠️ No se capturaron documentos en V2. FactScore será 0.")

                    status.update(label="Comparación Triple Completada", state="complete")
                    
                    # Render inmediato
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        st.markdown(f"**{n_v0}**")
                        st.caption(f"⏱️ {t_v0:.2f}s")
                        st.info(r_v0)
                    with c2:
                        st.markdown(f"**{n_v1}**")
                        st.caption(f"⏱️ {t_v1:.2f}s")
                        st.success(r_v1)
                        render_metrics(m_v1)
                    with c3:
                        st.markdown(f"**{n_v2}**")
                        st.caption(f"⏱️ {t_v2:.2f}s")
                        st.warning(r_v2)
                        render_metrics(m_v2)
                    
                    # Guardar sesion
                    st.session_state.messages_comp.append({
                        "role": "assistant",
                        "model_a_name": n_v0, "resp_a": r_v0, "time_a": t_v0, "metrics_a": m_v0,
                        "model_b_name": n_v1, "resp_b": r_v1, "time_b": t_v1, "metrics_b": m_v1,
                        "model_c_name": n_v2, "resp_c": r_v2, "time_c": t_v2, "metrics_c": m_v2,
                        "mode": compare_mode
                    })
                    
                else:
                    # ═══ DUAL COMPARISON ═══
                    parts = compare_mode.split(" vs ") # e.g. ["V0", "V1"]
                    label_a, label_b = parts[0], parts[1]
                    
                    # Run A
                    status.write(f"Ejecutando {label_a}...")
                    n_a, r_a, t_a, _, m_a = run_model_a_comparison(label_a, prompt, llm, rag_engine, agent_instance, use_metrics, status)
                    
                    # Run B
                    status.write(f"Ejecutando {label_b}...")
                    n_b, r_b, t_b, _, m_b = run_model_a_comparison(label_b, prompt, llm, rag_engine, agent_instance, use_metrics, status)
                    
                    status.update(label="Comparación Completada", state="complete")
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown(f"**{n_a}**")
                        st.caption(f"⏱️ {t_a:.2f}s")
                        st.info(r_a)
                        render_metrics(m_a)
                    with c2:
                        st.markdown(f"**{n_b}**")
                        st.caption(f"⏱️ {t_b:.2f}s")
                        st.success(r_b)
                        render_metrics(m_b)
                    
                    st.session_state.messages_comp.append({
                        "role": "assistant",
                        "model_a_name": n_a, "resp_a": r_a, "time_a": t_a, "metrics_a": m_a,
                        "model_b_name": n_b, "resp_b": r_b, "time_b": t_b, "metrics_b": m_b,
                        "mode": compare_mode
                    })
                    
            except Exception as e:
                import traceback
                traceback.print_exc()
                status.update(label="Error", state="error")
                st.error(f"Error Comparativa: {e}")
