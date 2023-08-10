import openai
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")
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
                                                                 "pongas \"Párrafo x:\" al inicio de cada párrafo. \n"
                                                                 
                                                                 "Ten en cuenta que el contenido del libro debe ser coherente y relevante "
                                                                 "para el título y los requisitos que te proporcione. Cuida el nivel. Si "
                                                                 "te digo que es para un público culto, no escribas para estudiantes. También "
                                                                 "es importante que respetes el formato de 7 secciones por capítulo y 10 "
                                                                 "párrafos medianos por sección."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
