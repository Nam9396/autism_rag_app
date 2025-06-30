import streamlit as st 
import os 

def sidebar():
    with st.sidebar:
        # General guide section
        
        st.session_state["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", None)

        show_citation = st.radio(
            "Xem dẫn nguồn của câu trả lời", 
            options=["Ẩn nguồn tài liệu", "Hiển thị nguồn tài liệu"], 
            help="Hiển thị các đoạn văn được dùng để tổng hợp câu trả lời. Chọn hiển thị sẽ làm tăng thời gian phản hồi."
        )

        st.session_state["show_citation"] = show_citation
