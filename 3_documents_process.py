# import streamlit as st

# from core.parsing import read_file
# from core.chunking import chunk_file
# from core.faiss_store import add_documents, save_store_local
# from components.ui import display_general_error, display_general_warning



# st.title("Số hóa văn bản")

# st.markdown("Tải lên file, số hóa nội dung và tạo cơ sở dữ liệu để truy xuất.")

# if "input_file" not in st.session_state:
#     st.session_state["input_file"] = None

# def handle_uploaded_files_change():
#     if not st.session_state["input_file"]:
#         st.session_state["input_file"] = None
#     else: 
#         del st.session_state["input_file"]

# uploaded_file = st.file_uploader(
#     label="Tải lên một file pdf", 
#     help="Chỉ xử lý file chứa nội dung có thể bôi đen và copy paste. Không chấp nhận file pdf chứa nội dung là hình ảnh scan.",
#     type=["pdf"], 
#     accept_multiple_files=False,
#     on_change=handle_uploaded_files_change
# )

# start_page, end_page = st.columns(2)

# with start_page:
#     start_page_number = st.number_input("Trang bắt đầu trích xuất", value=1, placeholder="Bắt đầu trích xuất từ trang 2, nhập 2")
#     start_page_number -= 1

# with end_page: 
#     end_page_number = st.number_input("Trang kết thúc trích xuất", value=1, placeholder="Kết thúc trích xuất tại trang 10, nhập 10")


# def process_docs():
#     try: 
#         st.session_state["input_file"] = read_file(file=uploaded_file, start_page_number=start_page_number, end_page_number=end_page_number)
#         st.toast("Hoàn thành đọc và làm sạch văn bản.")
#     except Exception as e:
#         display_general_error(e=e, message="Phát sinh lỗi trong quá trình đọc file. Xin đảm bảo file không bị gián đoạn, không mã hóa.")

# col1, col2, col3 = st.columns(3)

# with col2:
#     st.button(
#         "Xử lý văn bản",
#         use_container_width=True, 
#         on_click=process_docs,
#         disabled=True if not uploaded_file else False
#     )

# if not uploaded_file or not st.session_state["input_file"]:
#     st.stop()

# input_file = st.session_state.get("input_file", None)

# if input_file is None: 
#     st.stop()

# docs = input_file.docs

# if len(docs) == 0:
#     display_general_warning(message="File không có nội dung hoặc nội dung là hình ảnh scan. Bấm đặt lại, xóa file cũ và tải lên file có nội dung.")

# chunks_store = chunk_file(st.session_state["input_file"], chunk_size=300, chunk_overlap=50)

# if len(chunks_store) == 0:
#     display_general_warning(message="File không có nội dung hoặc nội dung là hình ảnh scan. Bấm đặt lại, xóa file cũ và tải lên file có nội dung.")

# with st.expander("Xem kết quả ban đầu"):
#     for doc in chunks_store:
#         st.write(doc.page_content)
#         st.write(doc.metadata)

# if st.button("Nhập liệu"):
#     add_documents(chunks_store)

# if st.button("Tạo thư mục"):
#     save_store_local()