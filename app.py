import streamlit as st
import ollama

st.title("Azure AI Chatbot")

# Reset button
if st.button("Reset Chat"):
    st.session_state.messages = []

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# Chat input
user_input = st.chat_input("Ask any question")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    response = ollama.chat(
        model="gemma2:2b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Answer clearly and simply."
            }
        ] + st.session_state.messages
    )

    ai_reply = response["message"]["content"]

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    st.chat_message("assistant").write(ai_reply)
