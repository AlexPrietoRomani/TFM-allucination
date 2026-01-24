import streamlit as st

st.set_page_config(page_title="TFM Chatbot", page_icon="🫐")

st.title("Chatbot Fitosanitario Arándanos")

st.info("Sistema iniciado. Seleccione configuración en el sidebar.")

with st.sidebar:
    st.header("Configuración")
    provider = st.selectbox("Proveedor", ["Gemini", "OpenRouter"])
    model = st.text_input("Modelo", value="gemini-1.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escribe tu consulta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        st.markdown(f"Echo ({provider}/{model}): {prompt}")
    
    st.session_state.messages.append({"role": "assistant", "content": f"Echo ({provider}/{model}): {prompt}"})
