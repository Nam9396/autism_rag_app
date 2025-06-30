import os
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY", None)
from requests.exceptions import HTTPError
from typing import TypedDict, List, Dict, Literal
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command

from core.functions.question_answer_chain import generate_answer
from core.prompts_models import get_evaluate_answer_model, evaluate_answer_prompt_template
from components.ui import display_general_error
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


class AnswerEvaluation(BaseModel):
    valid_answer: Literal[0, 1] = Field(
        description="Whether the answer is valid (1) or not (0). A valid answer directly and accurately answers the question."
    )
    justification: str = Field(
        description="Short explanation for why the answer is valid or not, based strictly on its relevance and factual correctness."
    )

evaluate_answer_model = get_evaluate_answer_model()

structured_llm = evaluate_answer_model.with_structured_output(AnswerEvaluation)

evaluate_answer_prompt = PromptTemplate(
    template=evaluate_answer_prompt_template, 
    input_variables=["question", "answer"]
)

evaluate_answer_chain = evaluate_answer_prompt | structured_llm


class OverallState(TypedDict):
    vn_question: str
    en_question: str
    message_history: List[Dict[str, str]]
    original_answer: str
    final_answer: str
    context: str
    justification: str


def retrieval_chain_node(state: OverallState):
    response = generate_answer(question=state["en_question"], message_history=state["message_history"])
    return { 
        "final_answer": response["answer"], 
        "context": "\n\n".join([
                    f"**{doc.metadata['file_name'].replace('.pdf', '')} - Trang: {doc.metadata['page']} - Đoạn: {doc.metadata['chunk']}** \n\n {doc.page_content}" 
                    for doc in response["context"]])
    }


def web_search_node(state: OverallState):
    try:
        response = tavily_client.search(
            query=state["vn_question"],
            topic="general",
            search_depth="advanced",
            include_answer="advanced",
            country="vietnam"
        )
        answer = response.get("answer", "Không thể đưa ra câu trả lời phù hợp. Xin thử lại bằng cách hỏi khác.")
        results = response.get("results", [])
        source_list = []
        if results:
            for source in results:
                source_list.append(f"URL: {source['url']} \n Nguồn: {source['content']}")
        else:
            source_list.append("Không tìm được nguồn thông tin phù hợp. Xin thử lại bằng cách hỏi khác.")

    except HTTPError as e:
        # status = e.response.status_code
        # error_detail = e.response.json().get("detail", {}).get("error", "Unknown error")
        display_general_error(e=e, message="Không thể trả lời câu hỏi (Lỗi tìm kiếm website). Xin thử lại bằng cách hỏi khác.")

    except Exception as e:
        display_general_error(e=e, message="Không thể trả lời câu hỏi (Lỗi tìm kiếm website). Xin thử lại bằng cách hỏi khác.")
    
    return { 
        "final_answer": answer + " **(Câu hỏi trả lời được tổng hợp từ các Website)**", 
        "context": "\n\n".join([source for source in source_list])
    }


# def is_answer_sufficient_node(state: OverallState):
#     response = evaluate_answer_chain.invoke({
#         "question": state["question"], 
#         "answer": state["answer"]
#     })
#     if response.valid_answer == 0: 
#         return "web_search"
#     else: 
#         return END

def check_answer(state: OverallState) -> Command[Literal["web_search"]]:
    response = evaluate_answer_chain.invoke({
        "question": state["vn_question"], 
        "answer": state["final_answer"]
    })
    if response.valid_answer == 0: 
        return Command(update={"justification": response.justification, "original_answer": state["final_answer"]}, goto="web_search")
    else:
        return Command(update={"justification": response.justification, "original_answer": state["final_answer"]}, goto=END )

graph = StateGraph(OverallState)

# graph.add_node("retrieval", retrieval_chain_node)
# graph.add_node("web_search", web_search_node)
# graph.add_edge(START, "retrieval")
# graph.add_conditional_edges(
#     "retrieval",
#     is_answer_sufficient_node,
#     {
#         END: END,
#         "web_search": "web_search" 
#     }
# )
# graph.add_edge("web_search", END)

graph.add_node("retrieval", retrieval_chain_node)
graph.add_node("web_search", web_search_node)
graph.add_node("check_answer", check_answer)
graph.add_edge(START, "retrieval")
graph.add_edge("retrieval", "check_answer")
graph.add_edge("check_answer", END)
graph.add_edge("web_search", END)

app = graph.compile()