# Lab 12 - Intro to LangSmith (with LangGraph)

A simple lab to get started with **LangSmith**, LangChain's platform for tracing, debugging, and monitoring LLM applications. The example app is built with **LangGraph**, so you will see each graph node as a step in the trace.

## What You Will Learn

- What LangSmith is and why tracing matters
- How to enable tracing with environment variables
- How LangGraph workflows are traced automatically (no extra code needed)
- How to trace a helper function with `@traceable`
- How to add a run name, tags, and metadata to a trace through the run `config`
- How to view traces in the LangSmith UI

## Prerequisites

- Python 3.11+ with your virtual environment activated
- A free LangSmith account: https://smith.langchain.com
- A LangSmith API key (Settings -> API Keys)
- An OpenAI API key
- Familiarity with Lab 11 (LangGraph)

## Setup

1. Install dependencies:

```bash
pip install langsmith langgraph langchain langchain-openai python-dotenv
```

2. Add these to your `.env` file (never commit it):

```
OPENAI_API_KEY=your-openai-key
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your-langsmith-key
LANGSMITH_PROJECT=gen-ai-labs
```

## Run the Lab

```bash
cd Lab-12-LangSmith
python langsmith_basics.py
```

## What the Code Does

`langsmith_basics.py` builds a small LangGraph workflow with two nodes:

```
START -> retrieve -> generate -> END
```

1. `retrieve` - calls `get_context()`, a fake retrieval step traced as a **tool** span with `@traceable`
2. `generate` - builds a prompt and calls the chat model with the retrieved context

The shared state (`question`, `context`, `answer`) is passed between nodes. Because LangGraph and LangChain integrate natively with LangSmith, setting `LANGSMITH_TRACING=true` is enough to log the graph run, each node, and every LLM call as nested spans. The previous `wrap_openai` wrapper is no longer needed.

## View Your Traces

1. Open https://smith.langchain.com
2. Go to **Tracing Projects** -> `gen-ai-labs`
3. Click the `assistant` run to see inputs, outputs, latency, token usage, and the nested steps (`retrieve`, `get_context`, `generate`, and the LLM call)

## Try It Yourself

- Change the question and compare the traces
- Add a third node (for example, a validator like in Lab 11) and watch it appear in the trace tree
- Add a conditional edge that retries `generate` and compare the traces
- Filter runs in the UI by the `lab-12` tag or the `topic` metadata

## Troubleshooting

- **No traces appear**: Check `LANGSMITH_TRACING=true` and that your API key is valid
- **Auth errors**: Re-check your `LANGSMITH_API_KEY` and `OPENAI_API_KEY`
- **Import errors**: Make sure `langgraph`, `langchain`, and `langchain-openai` are installed
- **Wrong project**: Confirm the `LANGSMITH_PROJECT` value

## Reference

- LangSmith docs: https://docs.langchain.com/langsmith
- LangGraph docs: https://docs.langchain.com/oss/python/langgraph/overview
