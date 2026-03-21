# Lab 4: Model Parameters & Output Parsing

This lab builds on **Lab 1** (Explore Closed Source Models), **Lab 2** (Explore LangChain), and **Lab 3** (Prompting Techniques). You'll learn to tune LLM parameters (temperature, top P, max tokens) and use LangChain's output parsers to extract structured data from model responses.

## Prerequisites

- **Lab 1 completed** — Environment, virtual environment, and API keys set up
- **Lab 2 completed** — Familiarity with LangChain prompts and chains
- **Lab 3 completed** — Understanding of prompt engineering fundamentals
- Python 3.11 or higher
- API keys configured in your `.env` file (OpenAI required; Gemini and Anthropic optional for token cost tracking)

## Getting Started

### 1. Pull the Latest Code

Before starting, ensure you have the latest code from the repository:

```bash
# Navigate to the project root
cd /path/to/Gen-AI-Agentic-AI-Labs

# Pull the latest changes
git pull origin main
```

> **Note:** Replace `main` with your default branch name if different (e.g., `master`).

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
cd "Lab-4-Model Parameters & Output Parsing Lab"

# Install dependencies
pip install -r requirements.txt
```

### 5. Environment Variables

Lab 4 uses the same `.env` file as previous labs. Ensure your `.env` contains:

```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here      # Optional - for token_cost_tracking.py
ANTHROPIC_API_KEY=your_anthropic_api_key_here # Optional - for token_cost_tracking.py
```

- **Notebooks** use **OpenAI GPT-4o-mini**
- **token_cost_tracking.py** compares costs across OpenAI, Google Gemini, and Anthropic Claude

## What You'll Learn

### Model Parameters
- **Temperature** — Controls randomness/creativity (low = factual, high = creative)
- **Top P** — Controls diversity via nucleus sampling (fewer vs more token options)
- **Max Tokens** — Limits output length for cost control and response management

### Output Parsers
- **StrOutputParser** — Clean string output (most common)
- **CommaSeparatedListOutputParser** — Extract lists from responses
- **JsonOutputParser** — Flexible JSON extraction
- **PydanticOutputParser** — Structured data with validation and type safety

### Bonus
- **Token Cost Tracking** — Compare token usage and pricing across different providers

## Usage

**Important:** Before running notebooks or scripts:
1. Pull the latest code: `git pull origin main`
2. Activate your virtual environment: `source venv/bin/activate`
3. Navigate to the lab directory: `cd "Lab-4-Model Parameters & Output Parsing Lab"`

### Run LLM Parameters Notebook

Explores temperature, top P, and max tokens with side-by-side comparisons:

```bash
jupyter notebook llm_parameters.ipynb
```

### Run Output Parsers Notebook

Demonstrates StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser, and PydanticOutputParser:

```bash
jupyter notebook output_parsers.ipynb
```

### Run Token Cost Tracking Script

Compares token usage and estimated cost across OpenAI, Gemini, and Claude:

```bash
python token_cost_tracking.py
```

Requires API keys for all three providers. The script gracefully handles missing keys and prints errors for unavailable providers.

## Project Structure

```
Lab-4-Model Parameters & Output Parsing Lab/
├── llm_parameters.ipynb         # Temperature, Top P, Max Tokens
├── output_parsers.ipynb         # Str, List, JSON, Pydantic parsers
├── token_cost_tracking.py       # Cross-provider token & cost comparison
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Key Concepts

| Resource | Topic | Key Components |
|----------|-------|----------------|
| `llm_parameters.ipynb` | Temperature | `init_chat_model(..., temperature=0.1)` |
| `llm_parameters.ipynb` | Top P | `init_chat_model(..., top_p=0.3)` |
| `llm_parameters.ipynb` | Max Tokens | `init_chat_model(..., max_tokens=50)` |
| `output_parsers.ipynb` | String Parser | `StrOutputParser()` |
| `output_parsers.ipynb` | List Parser | `CommaSeparatedListOutputParser()` |
| `output_parsers.ipynb` | JSON Parser | `JsonOutputParser()` |
| `output_parsers.ipynb` | Pydantic Parser | `PydanticOutputParser(pydantic_object=...)` |
| `token_cost_tracking.py` | Cost Tracking | Token usage, pricing per million tokens |

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Activate your virtual environment and run `pip install -r requirements.txt`

2. **API Key Errors**: Ensure your `.env` file is in the lab directory (or parent) and contains valid API keys

3. **Pydantic Import Error**: The output parsers notebook uses `PydanticOutputParser` — ensure `pydantic` is installed (included in requirements.txt)

4. **Kernel not found**: In Jupyter, select the Python kernel that has your virtual environment activated

5. **Git pull conflicts**: If you have local changes, stash them first: `git stash` then `git pull`, then `git stash pop`

## Notes

- Lab 4 extends the setup from Labs 1–3 — no additional API keys required for the notebooks (OpenAI only)
- **Token cost tracking** requires OpenAI, Google, and Anthropic keys; it will skip providers without valid keys
- Temperature and Top P are typically adjusted one at a time, not both simultaneously
- Use low temperature (0.1–0.3) for factual tasks; high (0.7–1.5) for creative tasks
- PydanticOutputParser provides validation and type safety—ideal for structured extraction
