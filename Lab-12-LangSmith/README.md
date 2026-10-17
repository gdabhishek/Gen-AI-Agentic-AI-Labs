# Lab 12 - Intro to LangSmith

A simple lab to get started with **LangSmith**, LangChain's platform for tracing, debugging, and monitoring LLM applications.

## What You Will Learn

- What LangSmith is and why tracing matters
- How to enable tracing with environment variables
- How to trace a function with `@traceable`
- How to auto-trace OpenAI calls with `wrap_openai`
- How to add tags and metadata to a trace
- How to view traces in the LangSmith UI

## Prerequisites

- Python 3.11+ with your virtual environment activated
- A free LangSmith account: https://smith.langchain.com
- A LangSmith API key (Settings -> API Keys)
- An OpenAI API key

## Setup

1. Install dependencies:

```bash
pip install langsmith openai python-dotenv
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

`langsmith_basics.py` builds a tiny assistant made of two steps:

1. `get_context()` - a fake retrieval step, traced as a **tool** span
2. `assistant()` - calls OpenAI with the context, traced as the parent run

Because the OpenAI client is wrapped with `wrap_openai`, every LLM call is logged automatically as a child span.

## View Your Traces

1. Open https://smith.langchain.com
2. Go to **Tracing Projects** -> `gen-ai-labs`
3. Click a run to see inputs, outputs, latency, token usage, and the nested steps

## Try It Yourself

- Change the question and compare the traces
- Add a new `@traceable` function and watch it appear in the trace tree
- Filter runs in the UI by the `lab-12` tag or the `topic` metadata

## Troubleshooting

- **No traces appear**: Check `LANGSMITH_TRACING=true` and that your API key is valid
- **Auth errors**: Re-check your `LANGSMITH_API_KEY` and `OPENAI_API_KEY`
- **Wrong project**: Confirm the `LANGSMITH_PROJECT` value

## Reference

- LangSmith docs: https://docs.langchain.com/langsmith
