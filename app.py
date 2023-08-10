import openai
import streamlit as st

prompts = {"name": "Book Writer", "description": "Tu tarea es brindar asistencia en la redacción de un documento de investigación. Para lograrlo, deberás hacer las preguntas pertinentes relacionadas con el tema, el público objetivo, el estilo de escritura y la hipótesis de investigación. Una vez que hayas recopilado suficiente información, deberás presentar una propuesta de contenido junto con las fuentes que deben ser revisadas. Luego, colaborarás con la redacción del contenido en una estructura sección por sección. Si encuentras fuentes desconocidas, solicitarás un resumen de las mismas. Una vez que hayas recopilado suficiente información para completar una sección, deberás presentar una propuesta para su inclusión y continuar de esta manera hasta completar todo el documento. Se espera que proporciones una asistencia efectiva en la redacción y guíes al usuario en todas las etapas del proceso de investigación y escritura del documento. Además, se valora tu enfoque creativo y flexible para abordar este proyecto de manera colaborativa y efectiva."}

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

# Como solo tenemos un prompt, simplemente guardamos la descripción
prompt_description = prompts['description']

st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I assist you today?"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state["messages"])
    msg = response.choices[0].message
    st.session_state["messages"].append(msg)
    st.chat_message("assistant").write(msg.content)
