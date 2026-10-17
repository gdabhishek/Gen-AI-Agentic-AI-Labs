"""Lab 12 - LangSmith basics.

Traces a tiny assistant so you can inspect it in the LangSmith UI.

Required environment variables (put them in your .env file):
    OPENAI_API_KEY
    LANGSMITH_API_KEY
    LANGSMITH_TRACING=true
    LANGSMITH_PROJECT=gen-ai-labs   (optional)
"""

from dotenv import load_dotenv
from openai import OpenAI
from langsmith import traceable
from langsmith.wrappers import wrap_openai

load_dotenv()

# Wrapping the client logs every OpenAI call automatically
client = wrap_openai(OpenAI())


@traceable(run_type="tool", name="get_context")
def get_context(question: str) -> str:
    """Fake retrieval step. In a real app this would query a vector store."""
    return "LangSmith is a platform for tracing, evaluating, and monitoring LLM apps."


@traceable(name="assistant", tags=["lab-12"], metadata={"topic": "langsmith-basics"})
def assistant(question: str) -> str:
    """Parent run: groups the retrieval step and the LLM call in one trace."""
    context = get_context(question)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Answer using this context:\n{context}"},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    answer = assistant("What is LangSmith used for?")
    print(answer)
    print("\nDone! Open https://smith.langchain.com to view the trace.")
