import streamlit as st
import requests
import json
from health_query_keywords import check_keywords

if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "show_error" not in st.session_state:
    st.session_state["show_error"] = False


def convert_to_messages(history):
    messages = []
    for entry in history:
        if entry.startswith("You:"):
            messages.append({"role": "user", "content": entry[5:]})
        elif entry.startswith("Bot:"):
            messages.append({"role": "assistant", "content": entry[5:]})
    return messages


def get_model_response():
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    messages = convert_to_messages(st.session_state.conversation)

    data = json.dumps(
        {"model": "llama3", "messages": messages, "stream": False}
    )

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()["message"]["content"]
    else:
        return "Error: The model API returned an unexpected response."


def clear_conversation():
    st.session_state.conversation = []


def ask_question(question):
    if not check_keywords(question):
        st.session_state["show_error"] = True
    else:
        st.session_state["show_error"] = False
        st.session_state.conversation.append(f"You: {question}")
        response = get_model_response()
        st.session_state.conversation.append(f"Bot: {response}")


st.title("Healt Query Chatbot")

st.button("Clear Conversation", type="primary", on_click=clear_conversation)


with st.form(key="chat_form"):
    user_input = st.text_input("You:")
    submit_button = st.form_submit_button(label="Send")

    if submit_button and user_input:
        ask_question(user_input)

if st.session_state["show_error"]:
    st.error(
        "I am a health assistant, please ask me health-related questions 😵‍💫",
        icon="🚨",
    )

sample_question_1 = st.button(
    "What are some effective methods for managing stress?",
    on_click=lambda: ask_question(
        "What are some effective methods for managing stress?"
    ),
)
sample_question_2 = st.button(
    "What first aid steps should I take for a minor burn?",
    on_click=lambda: ask_question(
        "What first aid steps should I take for a minor burn?"
    ),
)
sample_question_3 = st.button(
    "What are the symptoms of dehydration?",
    on_click=lambda: ask_question("What are the symptoms of dehydration?"),
)
st.divider()


for message in st.session_state.conversation:
    if message.startswith("You:"):
        st.markdown(f":red-background[😼: {message[5:]}]")
    else:
        st.markdown(f"🤖: {message[5:]}")
