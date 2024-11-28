import streamlit as st

def get_bot_response(user_input):
    return f"챗봇: 당신이 '{user_input}'라고 말씀하셨군요. 어떻게 도와드릴까요?"

st.title("간단한 챗봇 by TKJ")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("무엇이 궁금하신가요?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    bot_response = get_bot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

for i, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        st.text_area("사용자:", value=message["content"], height=70, disabled=True, key=f"user_message_{i}")
    else:
        st.text_area("챗봇:", value=message["content"], height=70, disabled=True, key=f"bot_message_{i}")