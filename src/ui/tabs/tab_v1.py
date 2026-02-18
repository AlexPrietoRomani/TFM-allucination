import streamlit as st
import time
from src.core.providers.factory import ProviderFactory
from src.ui.utils import render_metrics, calculate_metrics_sync

def render_tab_v1(rag_engine, provider: str, model_id: str, use_metrics: bool):
    """
    Renderiza la pestaña V1 (RAG Estándar).
    """
    st.subheader("Chat V1: RAG Estándar (Retrieval-Augmented)")
    st.caption("_El sistema busca documentos relevantes en Qdrant antes de generar la respuesta, reduciendo alucinaciones._")
    
    # Historial
    for msg in st.session_state.messages_v1:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if "time" in msg: st.caption(f"⏱️ {msg['time']:.2f}s")
            if "metrics" in msg: render_metrics(msg["metrics"])
            if "sources" in msg:
                with st.expander(f"📄 Fuentes ({len(msg['sources'])})"):
                    for d in msg['sources']:
                        st.caption(f"- {d.metadata.get('title','Doc')} ({d.metadata.get('source_id', '')})")

    # Input
    if prompt_v1 := st.chat_input("Pregunta a V1...", key="input_v1"):
        st.session_state.messages_v1.append({"role": "user", "content": prompt_v1})
        st.rerun()

    # Generación
    if st.session_state.messages_v1 and st.session_state.messages_v1[-1]["role"] == "user":
        prompt = st.session_state.messages_v1[-1]["content"]
        with st.chat_message("assistant"):
            status = st.status("Ejecutando Pipeline RAG...")
            t0 = time.time()
            try:
                llm = ProviderFactory.get_provider(provider, model_id)
                status.write("🔍 Buscando documentos...")
                # Paso 1: Retrieve
                docs = rag_engine.retrieve_context(prompt)
                
                status.write("📝 Generando respuesta...")
                # Paso 2: Generate
                rag_chain = rag_engine.get_chain(llm)
                resp = rag_chain.invoke(prompt)
                
                # Paso 3: Metrics
                met = calculate_metrics_sync(prompt, resp, docs, use_metrics, status)
                
                dt = time.time() - t0
                status.update(label="Listo", state="complete")
                
                # Render
                st.markdown(resp)
                st.caption(f"⏱️ {dt:.2f}s")
                render_metrics(met)
                
                with st.expander(f"📄 Fuentes ({len(docs)})"):
                    for d in docs:
                        st.caption(f"- {d.metadata.get('title','Doc')} ({d.metadata.get('source_id', '')})")
                
                # Save
                st.session_state.messages_v1.append({
                    "role": "assistant", "content": resp, "time": dt,
                    "metrics": met, "sources": docs
                })
            except Exception as e:
                 status.update(label="Error", state="error")
                 st.error(f"Error: {e}")
