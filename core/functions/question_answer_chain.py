
from core.prompts_models import get_synthesize_model, synthesize_answer_prompt_template
from core.faiss_store import create_mmr_retriever

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import trim_messages
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain



model = get_synthesize_model()

retriever = create_mmr_retriever(k=10, top_k=30, lambda_mult=0.4)


qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", synthesize_answer_prompt_template),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(model, qa_prompt) 

rag_chain = create_retrieval_chain(retriever, question_answer_chain)

trimmer = trim_messages(
    strategy="last",
    token_counter=len,
    max_tokens=5,
    start_on="human",
    end_on=("human", "tool"),
    include_system=True,
)

def generate_answer(question, message_history):
    trimmed_messages = trimmer.invoke(message_history)
    response = rag_chain.invoke({
        "input": question,
        "chat_history": trimmed_messages
    })
    return response


question_vn_en_template = """
Translate the following Vietnamese question into English so that it is very easy to understand.
Vietnames question: {question}
Translated English question: 
"""

question_vn_en_prompt = PromptTemplate(
    template=question_vn_en_template, 
    input_variables=["question"]
)

question_vn_en_chain = question_vn_en_prompt | model | StrOutputParser()
