# Lab 2: Explore LangChain

This lab builds on **Lab 1** (Explore Closed Source Models) and introduces **LangChain**—a framework for building applications with LLMs. You'll learn to create prompts, chains, and orchestrate multi-step workflows for a customer service agent.

## Prerequisites

- **Lab 1 completed** — You should have already set up your environment, virtual environment, and API keys (OpenAI, Anthropic, Google)
- Python 3.11 or higher
- API keys configured in your `.env` file (from Lab 1)

## Getting Started

### 1. Pull the Latest Code

Before starting, ensure you have the latest code from the repository:

```bash
# Navigate to the project root
cd /path/to/Gen-AI-Agentic-AI-Labs

# Pull the latest changes
git pull origin main
```

### 2. Navigate to the Parent Directory

Navigate to the parent directory (one level up from the lab folder):

```bash
# If you're currently in the lab folder, go up one directory:
cd ..

# Or navigate from the project root:
# cd "/path/to/Gen-AI-Agentic-AI-Labs"
```

### 3. Activate Virtual Environment

```bash
# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 4. Navigate to the Lab Directory and Install Dependencies

```bash
# Navigate to the lab folder
cd "Lab-2-Explore Langchain"

# Install dependencies
pip install -r requirements.txt
```

### 5. Environment Variables

Lab 2 uses the same `.env` file as Lab 1. Ensure your `.env` contains the API keys you need:

```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

## What You'll Learn

- **Prompt Templates** — Structured prompts with placeholders
- **Chains** — Composing LLM calls using the `|` pipeline operator
- **Sequential Chains** — Multi-step workflows (sentiment → category → response)
- **Parallel Chains** — Running independent steps concurrently with `RunnableParallel`

## Usage

**Important:** Before running any scripts:
1. Pull the latest code: `git pull origin main`
2. Activate your virtual environment: `source venv/bin/activate`
3. Navigate to the lab directory: `cd "Lab-2-Explore Langchain"`

### Run Basic LangChain Example

Introduces prompt templates and simple chains:

```bash
python explore_langchain.py
```

### Run Customer Service Agent (Sequential)

A sequential chain that analyzes sentiment, categorizes the issue, then generates a response:

```bash
python customer_service_agent.py
```

### Run Customer Service Agent (Parallel)

The same workflow but runs sentiment analysis and category classification **in parallel** for better performance:

```bash
python customer_service_agent_parallel.py
```

## Project Structure

```
Lab-2-Explore Langchain/
├── explore_langchain.py           # Basic LangChain: prompts and chains
├── customer_service_agent.py      # Sequential chain (sentiment → category → response)
├── customer_service_agent_parallel.py  # Parallel chain (RunnableParallel)
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Key Concepts

| File | Concept |
|------|---------|
| `explore_langchain.py` | `PromptTemplate`, `chain = prompt \| llm` |
| `customer_service_agent.py` | `RunnablePassthrough.assign()`, sequential chaining |
| `customer_service_agent_parallel.py` | `RunnableParallel`, parallel execution |

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Activate your virtual environment and run `pip install -r requirements.txt`

2. **API Key Errors**: Ensure your `.env` file is in the lab directory (or parent) and contains valid API keys

3. **Import Errors**: Lab 2 uses `langchain.chat_models.init_chat_model` — ensure all packages in `requirements.txt` are installed

4. **Git pull conflicts**: If you have local changes, stash them first: `git stash` then `git pull`, then `git stash pop`

## Notes

- Lab 2 extends the API setup from Lab 1 — no additional API keys are required if you completed Lab 1
- API usage may incur costs depending on your usage
- The parallel version (`customer_service_agent_parallel.py`) is more efficient as it runs independent LLM calls concurrently
