import streamlit as st
from core.functions.question_answer_chain import question_vn_en_chain
from core.functions.generate_answer_graph import app
from components.ui import display_general_error

st.header("Hỏi đáp về Tự kỷ")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Đặt câu hỏi về rối loạn phổ tự kỷ"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Đang suy nghĩ ...", show_time=True):
            try:
                english_question = question_vn_en_chain.invoke({"question": prompt})
                response = app.invoke({
                    "vn_question": prompt,
                    "en_question": english_question,
                    "message_history": st.session_state.messages
                })
                answer = response["final_answer"]
                # st.write(response["original_answer"])
                # st.write(response["justification"])
                st.write(answer)

                if st.session_state["show_citation"] == "Hiển thị nguồn tài liệu":
                    with st.expander("Nguồn tài liệu"):
                        st.markdown(response["context"])

            except Exception as e:
                display_general_error(e=e, message="Phát sinh lỗi khi yêu cầu AI trả lời câu hỏi. Xin đảm bảo kết nối mạng, cung cấp API key và thử lại sau.")

    st.session_state.messages.append({"role": "assistant", "content": answer})

