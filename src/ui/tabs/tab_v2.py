import streamlit as st
import time
import asyncio
from src.ui.utils import render_metrics, calculate_metrics_sync, run_agent_v2

def render_tab_v2(agent_instance, provider: str, model_id: str, use_metrics: bool):
    """
    Renderiza la pestaña V2 (Agente Autónomo).
    """
    st.subheader("Chat V2: Agente Autónomo (LangGraph)")
    st.caption("_Agente con ciclos de auto-corrección: si detecta una alucinación, reescribe la respuesta automáticamente._")
    
    # Historial
    for msg in st.session_state.messages_v2:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "time" in msg: st.caption(f"⏱️ {msg['time']:.2f}s")
            if "metrics" in msg: render_metrics(msg["metrics"])
            if "steps" in msg: 
                with st.expander("🔍 Trazabilidad (Pasos del Agente)"):
                    st.json(msg["steps"])

    # Input
    if prompt_v2 := st.chat_input("Pregunta a V2...", key="input_v2"):
        st.session_state.messages_v2.append({"role": "user", "content": prompt_v2})
        st.rerun()

    # Generación
    if st.session_state.messages_v2 and st.session_state.messages_v2[-1]["role"] == "user":
        prompt = st.session_state.messages_v2[-1]["content"]
        with st.chat_message("assistant"):
            status = st.status("Agente V2 Pensando...")
            t0 = time.time()
            try:
                # Ejecutar Agente V2 de forma asíncrona pero dentro del loop de Streamlit
                # run_agent_v2 retorna (response, docs, log_steps)
                resp, docs, steps = asyncio.run(run_agent_v2(agent_instance, prompt, status))
                
                # Calcular Métricas
                # Nota: FactScore requiere documentos recuperados. 
                # Si 'docs' está vacío, FactScore será 0.
                if not docs:
                    status.warning("⚠️ No se recuperaron documentos visibles (quizás el agente no usó retrieva o no se capturaron). FactScore será 0.")
                    
                met = calculate_metrics_sync(prompt, resp, docs, use_metrics, status)
                
                dt = time.time() - t0
                status.update(label="Listo", state="complete")
                
                # Render Final
                st.markdown(resp)
                st.caption(f"⏱️ {dt:.2f}s")
                render_metrics(met)
                
                with st.expander("🔍 Trazabilidad (Pasos del Agente)"):
                    st.json(steps)
                
                # Guardar en historial
                st.session_state.messages_v2.append({
                    "role": "assistant", "content": resp, "time": dt,
                    "metrics": met, "steps": steps
                })
            except Exception as e:
                status.update(label="Error", state="error")
                st.error(f"Error V2: {e}")
