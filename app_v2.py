import streamlit as st
import asyncio
from src.agent.graph import AgentGraph
from src.core.providers.factory import ProviderFactory

# Config
st.set_page_config(page_title="Agente RAG V2 (Autónomo)", layout="wide")
st.title("🤖 Agente RAG V2: Mitigación Activa")

# Inicializar Grafo
@st.cache_resource
def get_agent():
    return AgentGraph()

agent = get_agent()

# Historial
if "messages_v2" not in st.session_state:
    st.session_state.messages_v2 = []

# Mostrar historial
for msg in st.session_state.messages_v2:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "steps" in msg:
            with st.expander("🛠️ Trazabilidad del Agente"):
                st.json(msg["steps"])

# Input
if prompt := st.chat_input("Pregunta al Agente V2..."):
    st.session_state.messages_v2.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        status_box = st.status("🧠 Agente pensando...", expanded=True)
        resp_content = ""
        steps_log = []
        
        try:
            # Ejecutar grafo asíncrono
            # En streamlit sync, usamos asyncio.run o loop
            async def run_agent():
                final_state = None
                log = []
                # astream events para ver progreso
                async for event in agent.app.astream_events({"question": prompt}, version="v1"):
                    kind = event["event"]
                    name = event["name"]
                    
                    if kind == "on_chain_start" and name in ["retrieve", "generate", "grade", "classify", "chitchat"]:
                        status_box.write(f"▶️ Ejecutando nodo: **{name}**")
                        log.append(f"Start: {name}")
                        
                    if kind == "on_chain_end" and name == "grade":
                        # Intentar capturar output del grade
                        data = event["data"].get("output")
                        if data:
                            score = data.get("faithfulness_score")
                            reason = data.get("hallucination_reason")
                            status_box.markdown(f"📊 **Evaluación**: Score {score:.2f} | {reason}")
                            log.append({"node": "grade", "score": score, "reason": reason})

                # Obtener resultado final
                final_state = await agent.app.ainvoke({"question": prompt})
                return final_state, log

            # Hack para correr async en streamlit
            final_res, steps = asyncio.run(run_agent())
            
            resp_content = final_res.get("generation", "Error generando respuesta.")
            st.markdown(resp_content)
            
            status_box.update(label="¡Completado!", state="complete", expanded=False)
            
            # Guardar
            st.session_state.messages_v2.append({
                "role": "assistant", 
                "content": resp_content,
                "steps": steps
            })
            
        except Exception as e:
            st.error(f"Error: {e}")

