import openai
import streamlit as st

# Configuración de Sidebar
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

# Título del chatbot
st.title("💬 Chatbot")

# Prompt inicial invisible para el usuario
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Tu tarea es escribir un libro para mí. Primero, por favor, pregúntame "
                                                                     "el título del libro y la audiencia. Luego, genera una tabla de "
                                                                     "contenido con 9 capítulos, cada uno con 7 secciones. Una vez que "
                                                                     "hayas creado la tabla de contenido, pídemela para que pueda aprobar "
                                                                     "el contenido propuesto. Si no apruebo alguna sección, por favor, "
                                                                     "propón una alternativa. Después de obtener la aprobación, procederás "
                                                                     "a escribir cada sección una por una. Es decir, primero la sección 1.1, "
                                                                     "luego la 1.2 y así sucesivamente. Cada sección debe tener 10 párrafos "
                                                                     "de mediana extensión. Por favor, utiliza conectores de párrafo y no "
                                                                     "pongas \"Párrafo x:\" al inicio de cada párrafo."}]

# Imprime los mensajes del usuario y del asistente del chat
for msg in st.session_state.get("messages", []):
    if msg["role"] == "user":
        st.chat_message(msg["role"]).write(msg["content"])

# Pasos cuando el usuario ingreso un nuevo mensaje
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Por favor, agrega tu clave de API de OpenAI para continuar.")
        st.stop()

    # Configura la clave de API de OpenAI y agrega el mensaje del usuario al historial del chat
    openai.api_key = openai_api_key
    st.session_state["messages"].append({"role": "user", "content": prompt})

     # Modelado de la solicitud con el historial completo del chat actual
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=st.session_state.get("messages", []))
    
    # Añade la respuesta del asistente al historial del chat y imprímela
    msg = response.choices[0].message
    st.session_state["messages"].append(msg)
    st.chat_message("assistant").write(msg["content"])
