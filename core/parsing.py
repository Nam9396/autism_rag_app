from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List
from io import BytesIO
from copy import deepcopy
import fitz
import re
from hashlib import md5
import streamlit as st
from langchain_core.documents.base import Document


class File(ABC): 
    def __init__(
        self, 
        name: str, 
        id: str, 
        metadata: Optional[Dict[str, Any]] = None,
        docs: Optional[List[Document]] = None
    ):
        self.name = name
        self.id = id 
        self.metadata = metadata or {}
        self.docs = docs or {}
    
    @classmethod
    @abstractmethod
    def from_file(cls, file: BytesIO, removed_words: List[str]) -> "File":
        """Create a file object holding information about the file"""
        pass
    
    def __repr__(self):
        return f"File(name={self.name}, id={self.id}, metadata={self.metadata})"

    def copy(self):
        return self.__class__(
            name=self.name, 
            id=self.id,
            docs=deepcopy(self.docs),
            metadata=deepcopy(self.metadata)
        ) 

def clean_pdf_for_llm(text):
    # Normalize line endings
    text = text.replace('\r\n', '\n')
    # Fix hyphenated words split across lines
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    # Mark numbered or bulleted list items (so we don't flatten them later)
    # Add a placeholder before list item
    text = re.sub(r'\n(\s*\d+\.\s*)', r'[LIST_BREAK]\1', text)
    text = re.sub(r'\n(\s*[-●•■]\s*)', r'[LIST_BREAK]\1', text)
    # Mark real paragraph breaks (2 or more newlines)
    text = re.sub(r'\n{2,}', '[PARA_BREAK]', text)
    # Flatten remaining newlines (soft line breaks)
    text = re.sub(r'\n', ' ', text)
    # Restore paragraph breaks
    text = text.replace('[PARA_BREAK]', '\n\n')
    # Restore list items on new lines
    text = text.replace('[LIST_BREAK]', '\n')
    # Clean up multiple spaces
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


class PdfFile(File):
    @classmethod
    def from_file(cls, file: BytesIO, start_page_number: int, end_page_number: int) -> "PdfFile":
        docs = []
        with fitz.open(stream=file.read(), filetype="pdf") as pages: 
            for i in range(start_page_number, end_page_number):
                text = pages[i].get_text("text")
                text = clean_pdf_for_llm(text)
                doc = Document(page_content=text)
                doc.metadata["page"] = i + 1
                docs.append(doc)
        file.seek(0) # trỏ về lại phần đầu của file, vì con trỏ đã về cuối trong quá trình đọc file, mục đích vì sao thì mình không hiểu, bước đóng file nằm ở đâu
        return cls(
            name=file.name, 
            id=md5(file.read()).hexdigest(),
            docs=docs # ở đây docs chưa từng text box ở mỗi trang thuộc một file, các text box này phải có nội dung tối thiểu là 200 characters
        )
    
# file là BytesIO: objects are in-memory streams and are automatically cleaned up by Python's garbage collector when no longer referenced
# pages là sản phẩn của fitz.open() nên cần đóng lại

@st.cache_data(show_spinner=True)  
def read_file(file: BytesIO, start_page_number: int, end_page_number: int) -> File:
    # read_files chứa các instance về mỗi văn bản, mỗi instance chứa docs là một list các text block từ các page (thông tin định vị nằm trong metadata)
    pdf_file = PdfFile.from_file(file, start_page_number, end_page_number)
    return pdf_file