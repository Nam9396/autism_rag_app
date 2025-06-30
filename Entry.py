import streamlit as st
from components.sidebar import sidebar

st.set_page_config(layout="centered", initial_sidebar_state="auto")

question_answer_page = st.Page("1_question_answer.py", title="Hỏi đáp", icon=":material/forum:")
introduction_page = st.Page("2_introduction.py", title="Giới thiệu", icon=":material/emoji_people:")
# documents_process_page = st.Page("3_documents_process.py", title="Xử lý văn bản", icon=":material/add_notes:")


pg = st.navigation([
    question_answer_page,
    introduction_page, 
    # documents_process_page
])

sidebar()

pg.run()


