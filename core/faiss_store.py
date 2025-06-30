import os
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
from uuid import uuid4
import streamlit as st
from typing import List

from langchain_openai import OpenAIEmbeddings
import faiss
from langchain_core.documents.base import Document
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

from components.ui import display_general_error

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", api_key=OPENAI_API_KEY)

index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)


def add_documents(docs: List[Document]):
    uuids = [str(uuid4()) for _ in range(len(docs))]
    try:
        with st.spinner("Đang nhập và số hóa dữ liệu ...", show_time=True): 
            vector_store.add_documents(documents=docs, ids=uuids)
            st.toast("Hoàn thành nhập dữ liệu vào FAISS vector store")
    except Exception as e: 
        display_general_error(e=e, message="Phát lỗi trong quá trình nhập dữ liệu vào FAISS vector store")


def save_store_local():
    try:
        vector_store.save_local("faiss_index")
        st.toast("Hoàn thành tạo FAISS Index")
    except Exception as e: 
        display_general_error(e=e, message="Phát lỗi trong quá trình tạo FAISS index")

@st.cache_resource(show_spinner=True)
def create_mmr_retriever(k: int, top_k: int, lambda_mult: int):
    new_vector_store = FAISS.load_local(
        "faiss_index", embeddings, allow_dangerous_deserialization=True
    )
    return new_vector_store.as_retriever(
        search_type="mmr", 
        search_kwargs={"k": k, "fetch_k": top_k, "lambda_mult": lambda_mult}
    )