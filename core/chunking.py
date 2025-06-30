from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_core.documents.base import Document
import streamlit as st
import core.parsing as parsing
from core.parsing import File
from typing import List


def chunk_file(file: File, chunk_size: int, chunk_overlap: int) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap, 
        separators=[r"\n\n", r"\n", r"(?<=[.?!])\s+"],  # Order matters! Larger breaks should come first
        is_separator_regex=True
    )

    docs = []

    for doc in file.docs: 
        chunks = text_splitter.split_text(doc.page_content)
        for i, chunk in enumerate(chunks):
            final_doc = Document(page_content=chunk)
            final_doc.metadata["file_name"] = file.name
            final_doc.metadata["page"] = doc.metadata.get("page", "Undefined")
            final_doc.metadata["chunk"] = i + 1
            docs.append(final_doc)

    return docs
