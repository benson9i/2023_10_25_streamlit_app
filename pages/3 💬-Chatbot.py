import openai
import streamlit as st
from streamlit_lottie import st_lottie
import json

# ---- Page setup ----
st.title("🤖 ChatGPT Clone")
st.subheader("This is an AI chatbot built on the OpenAI GPT model")

# ---- Lottie Animation Below Chat ----
def load_lottiefil(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_chat = load_lottiefil("lottie/chat_lottie.json")

col3, col4, col5 = st.columns([1,2,1], gap="small")
with col3:
    st.write("")

with col4:
    st_lottie(lottie_chat, height=300, width=300)

with col5:
    st.write("")


# ---- Initial setup for icons ----
if "user_icon" not in st.session_state:
    st.session_state.user_icon = "🙎🏻‍♂️"

if "bot_icon" not in st.session_state:
    st.session_state.bot_icon = "🤖"

# ---- Sidebar inputs ----
openai_api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
temperature = st.sidebar.slider("Select temperature:", min_value=0.0, max_value=1.0, value=0.5, step=0.05)

if openai_api_key:
    openai.api_key = openai_api_key
else:
    st.sidebar.warning("Please provide an OpenAI API key to proceed.")
    st.stop()

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- Display previous messages ----
for message in st.session_state.messages:
    with st.chat_message(st.session_state.user_icon if message["role"] == "user" else st.session_state.bot_icon):
        st.markdown(message["content"])

# ---- Chat Input Field ----
if prompt := st.chat_input("WWrite something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message(st.session_state.user_icon):  # Use the user_icon from session_state
        st.markdown(prompt)

    with st.chat_message(st.session_state.bot_icon):  # Use the bot_icon from session_state
        message_placeholder = st.empty()
        full_response = ""
        try:
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
                temperature=temperature,  # Use the temperature value from the sidebar
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
        except openai.error.AuthenticationError:
            st.sidebar.error("Invalid OpenAI API key. Please check and try again.")
            st.stop()
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
