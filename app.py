import openai
import streamlit as st
import prompts

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    selected_prompt = st.selectbox('Select a prompt', options=[p["name"] for p in prompts.prompts_list])

# Encontrar la descripción del prompt seleccionado
for prompt_obj in prompts.prompts_list:import openai
import streamlit as st
import promptsimport openai
import streamlit as st

prompts = [
    {"name": "Book Writer", "description": "Your task is to write a book..."},
    {"name": "Research Assistant", "description": "Your task is to assist in writing a research paper..."},
    # Más prompts aquí
]

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    selected_prompt = st.selectbox('Select a prompt', options=[p["name"] for p in prompts])

# Encontrar la descripción del prompt seleccionado
prompt_description = next((p["description"] for p in prompts if p["name"] == selected_prompt), None)

st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

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
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    selected_prompt = st.selectbox('Select a prompt', options=[p["name"] for p in prompts.prompts_list])

# Encontrar la descripción del prompt seleccionado
for prompt_obj in prompts.prompts_list:
    if prompt_obj["name"] == selected_prompt:
        selected_prompt_desc = prompt_obj["description"]
        break

st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if user_msg := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": user_msg})
    st.chat_message("user").write(user_msg)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "system", "content": "This is a OpenAI GPT-3 Assistant."}] + st.session_state["messages"],
    )
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
    if prompt_obj["name"] == selected_prompt:
        selected_prompt_desc = prompt_obj["description"]
        break

st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": selected_prompt_desc}] # set the initial message as the selected prompt

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if user_msg := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": user_msg})
    st.chat_message("user").write(user_msg)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages[-4:])
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
