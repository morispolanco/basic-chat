import openai
import streamlit as st
import prompts

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    selected_prompt = st.selectbox('Select a prompt', options=[p["name"] for p in prompts.prompts_list])

# Encontrar la descripción del prompt seleccionado
for prompt_obj in prompts.prompts_list:import openai
import streamlit as st
import prompts

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
