# import streamlit as st
# from uuid import uuid4
# from typing import List, Dict, Any
# from components.ui import display_general_error

# from langchain_openai import OpenAIEmbeddings
# from langchain_core.documents.base import Document
# from langchain_chroma import Chroma


# @st.cache_resource(show_spinner=True)
# def create_chroma_store():
#     return Chroma(
#         collection_name="asd_book_collection",
#         embedding_function=OpenAIEmbeddings(model="text-embedding-3-large"),
#         persist_directory="./asd_book_db",  # Where to save data locally, remove if not necessary
#     )

# chroma_store = create_chroma_store()

# def add_documents(docs: List[Document]):
#     uuids = [str(uuid4()) for _ in range(len(docs))]
#     try:
#         with st.spinner("Đang nhập và số hóa dữ liệu ...", show_time=True): 
#             chroma_store.add_documents(documents=docs, ids=uuids)
#             st.toast("Hoàn thành nhập dữ liệu vào Chroma vector store")
#     except Exception as e: 
#         display_general_error(e=e, message="Phát lỗi trong quá trình nhập dữ liệu vào Chroma vector store")


# def create_mmr_retriever(k: int, top_k: int, lambda_mult: int):
#     return chroma_store.as_retriever(
#         search_type="mmr", 
#         search_kwargs={"k": k, "fetch_k": top_k, "lambda_mult": lambda_mult}
#     )


# cách này trả về top_k trước, rồi lọc ra k nhưng khác biệt với nhau, cách này đảm bảo tính đa dạng của vector
# def mmr_search(query: str, k: int, top_k: int, lambda_mult: int, filter: Dict[str, Any] = None) -> List[Document]:
#     try: 
#         retriever = chroma_store.as_retriever(
#             search_type="mmr",
#             search_kwargs={"k": k, "fetch_k": top_k, "lambda_mult": lambda_mult}
#         )
#         relevant_documents = retriever.invoke(query, filter)
#         return relevant_documents
#     except Exception as e: 
#         display_general_error(e=e, message="Phát lỗi trong quá trình truy xuất mmr_search")




# cách này là default với consine, đảm bảo luôn có vector trả về nhưng có thể bị lặp lại và không đa dạng
# def similarity_search(query: str, k: int, filter: Dict[str, Any] = None) -> List[Document]:
#     try: 
#         relevant_documents = chroma_store.similarity_search(query=query, k=k, filter=filter)
#         return relevant_documents
#     except Exception as e: 
#         display_general_error(e=e, message="Phát lỗi trong quá trình truy xuất similarity_search")


# cách này chỉ lọc ra các vector thật sự có điểm số liên quan > 0.8. nó đảm bảo tính liên quan nhưng có thể trả về kết quả 0. Dùng khi app cần tính chính xác cao, thà không có kết quả hơn là có kết quả sai
# nếu không có relevant docs, trả về empty list
# def similarity_score_threshold_search(query: str, filter: Dict[str, Any] = None) -> List[Document]:
#     try: 
#         retriever = chroma_store.as_retriever(
#             search_type="similarity_score_threshold",
#             search_kwargs={'score_threshold': 0.75}
#         )
#         relevant_documents = retriever.invoke(query, filter)
#         return relevant_documents
#     except Exception as e: 
#         display_general_error(e=e, message="Phát lỗi trong quá trình truy xuất similarity_score_threshold_search")
