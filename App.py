import streamlit as st

#제목
st.title('나의 첫 streamlit app 배포')

#헤더
st.header("환영합니다")

#몸통(텍스트)
st.write("streamlit은 정말 쉽습니다!")

name = st.text_input('이름을 입력하세요: ')
if name:
    st.write(f"안녕하세요, {name}님!")

if st.button('클릭하세요'):
    st.snow()
    st.success("축하합니다.")