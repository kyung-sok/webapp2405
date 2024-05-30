# 설치 필요
# pip install langchain
import streamlit as st
from langchain_community.llms import OpenAI
import time
from streamlit import caching

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

# OpenAI API 키 입력
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# 캐싱을 통해 API 키를 저장
@st.cache_data(allow_output_mutation=True)
def get_openai_api_key():
    return openai_api_key

# API 응답 생성 함수
def generate_response(input_text, api_key):
    try:
        llm = OpenAI(temperature=0.7, openai_api_key=api_key)
        response = llm(input_text)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# 폼을 통한 입력
with st.form('my_form'):
    text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
    submitted = st.form_submit_button('Submit')
    
    if submitted:
        # API 키 유효성 검사
        if not openai_api_key.startswith('sk-'):
            st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
        else:
            # 로딩 상태 표시
            with st.spinner('AI 응답 생성 중...'):
                api_key = get_openai_api_key()
                response = generate_response(text, api_key)
                st.info(response)

# API 키가 제대로 입력되지 않은 경우 경고 메시지 표시
if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
