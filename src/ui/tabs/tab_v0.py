import streamlit as st
import time
from src.core.providers.factory import ProviderFactory

def render_tab_v0(provider: str, model_id: str):
    """
    Renderiza la pestaña V0 (Baseline) - Chat directo sin contexto.
    """
    st.subheader("Chat V0: Modelo Base (Sin Contexto)")
    st.caption("_El LLM responde directamente sin acceso a documentos. Útil como línea base para medir mejoras._")
    
    # Mostrar historial
    for msg in st.session_state.messages_v0:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "time" in msg: st.caption(f"⏱️ {msg['time']:.2f}s")

    # Input usuario
    if prompt_v0 := st.chat_input("Pregunta a V0...", key="input_v0"):
        st.session_state.messages_v0.append({"role": "user", "content": prompt_v0})
        st.rerun()

    # Generación respuesta
    if st.session_state.messages_v0 and st.session_state.messages_v0[-1]["role"] == "user":
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
                status.update(label="Error", state="error")
                st.error(f"Error: {e}")
