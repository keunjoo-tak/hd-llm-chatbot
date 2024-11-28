import streamlit as st

# 챗봇 응답을 생성하는 함수
def get_bot_response(user_input):
    # 여기에 실제 챗봇 로직을 구현할 수 있습니다.
    # 이 예제에서는 간단한 응답만 반환합니다.
    return f"챗봇: 당신이 '{user_input}'라고 말씀하셨군요. 어떻게 도와드릴까요?"

# 스트림릿 앱 구성
st.title("간단한 챗봇")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 사용자 입력 받기
user_input = st.text_input("무엇이 궁금하신가요?")

# 사용자가 입력을 제출했을 때
if user_input:
    # 사용자 메시지 저장
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 챗봇 응답 생성
    bot_response = get_bot_response(user_input)
    
    # 챗봇 응답 저장
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# 대화 내용 표시
for message in st.session_state.messages:
    if message["role"] == "user":
        st.text_area("사용자:", value=message["content"], height=50, disabled=True)
    else:
        st.text_area("챗봇:", value=message["content"], height=50, disabled=True)