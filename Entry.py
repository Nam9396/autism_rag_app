import streamlit as st
from components.sidebar import sidebar

st.set_page_config(layout="centered")

introduction_page = st.Page("1_introduction.py", title="Giới thiệu", icon=":material/emoji_people:")
question_answer_page = st.Page("2_question_answer.py", title="Hỏi đáp", icon=":material/forum:")
# documents_process_page = st.Page("3_documents_process.py", title="Xử lý văn bản", icon=":material/add_notes:")


pg = st.navigation([
    introduction_page, 
    question_answer_page,
    # documents_process_page
])

sidebar()

pg.run()


