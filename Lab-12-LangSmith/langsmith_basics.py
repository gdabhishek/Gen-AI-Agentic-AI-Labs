"""Lab 12 - LangSmith basics with LangGraph.

Builds a small LangGraph workflow (retrieve -> generate) and traces it in
LangSmith so you can inspect every node in the UI.

Required environment variables (put them in your .env file):
    OPENAI_API_KEY
    LANGSMITH_API_KEY
    LANGSMITH_TRACING=true
    LANGSMITH_PROJECT=gen-ai-labs   (optional)
"""

from dotenv import load_dotenv
from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from langsmith import traceable

load_dotenv()

# LangChain models are traced automatically when LANGSMITH_TRACING=true,
# so there is no need for wrap_openai anymore.
llm = init_chat_model("gpt-4o-mini", model_provider="openai")


# ---------- State ----------
class AssistantState(TypedDict):
    question: str
    context: str
    answer: str


# ---------- Helper traced with @traceable ----------
@traceable(run_type="tool", name="get_context")
def get_context(question: str) -> str:
    """Fake retrieval step. In a real app this would query a vector store."""
    return "LangSmith is a platform for tracing, evaluating, and monitoring LLM apps."


# ---------- Nodes ----------
def retrieve(state: AssistantState):
    """Node 1: fetch context for the question."""
    print("Retrieving context")
    return {"context": get_context(state["question"])}


def generate(state: AssistantState):
    """Node 2: answer the question using the retrieved context."""
    print("Generating answer")
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Answer using this context:\n{context}"),
            ("user", "{question}"),
        ]
    )
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke(
        {"context": state["context"], "question": state["question"]}
    )
    return {"answer": answer}


# ---------- Graph ----------
workflow = StateGraph(AssistantState)
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)

workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

app = workflow.compile()


if __name__ == "__main__":
    # run_name, tags and metadata show up on the root run in LangSmith
    result = app.invoke(
        {"question": "What is LangSmith used for?"},
        config={
            "run_name": "assistant",
            "tags": ["lab-12"],
            "metadata": {"topic": "langsmith-basics"},
        },
    )
    print(result["answer"])
    print("\nDone! Open https://smith.langchain.com to view the trace.")
