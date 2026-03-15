# Lab 3: Prompting Techniques

This lab builds on **Lab 1** (Explore Closed Source Models) and **Lab 2** (Explore LangChain). You'll master the art of **prompt engineering** through hands-on practice with LangChain—learning how to structure effective prompts and apply professional prompting strategies.

## Prerequisites

- **Lab 1 completed** — Environment, virtual environment, and API keys set up
- **Lab 2 completed** — Familiarity with LangChain prompts and chains
- Python 3.11 or higher
- API keys configured in your `.env` file (OpenAI required for this lab)

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
cd "Lab-3-Prompting _techniques"

# Install dependencies
pip install -r requirements.txt
```

### 5. Environment Variables

Lab 3 uses the same `.env` file as Lab 1 and Lab 2. Ensure your `.env` contains:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

This lab uses **OpenAI GPT-4o-mini** for all examples.

## What You'll Learn

- **Anatomy of a Good Prompt** — Context, Task, Format, Constraints (C-T-F-C framework)
- **Role Assignment** — Giving the AI expertise and perspective via system messages
- **Few-Shot Prompting** — Teaching desired format and style with examples
- **Chain-of-Thought** — Step-by-step reasoning for complex tasks
- **Output Format Control** — JSON, Markdown tables, structured bullet points
- **Prompt Chaining** — Breaking complex tasks into multi-step pipelines
- **Real-World Use Cases** — Professional email writing, content creation

## Usage

**Important:** Before running the notebook:
1. Pull the latest code: `git pull origin main`
2. Activate your virtual environment: `source venv/bin/activate`
3. Navigate to the lab directory: `cd "Lab-3-Prompting _techniques"`

### Run the Jupyter Notebook

```bash
jupyter notebook "Prompting Techniques.ipynb"
```

Or with JupyterLab:

```bash
jupyter lab "Prompting Techniques.ipynb"
```

Execute the cells in order. The notebook includes:
- **7 sections** covering core prompting techniques
- **5 hands-on exercises** for you to complete
- **Real-world examples** (code review, product descriptions, business decisions, email writing)

## Project Structure

```
Lab-3-Prompting _techniques/
├── Prompting Techniques.ipynb    # Main lab notebook
├── requirements.txt              # Python dependencies
└── README.md                    # This file
```

## Key Concepts

| Section | Technique | LangChain Components |
|---------|-----------|------------------------|
| 1 | Anatomy of a Good Prompt | Weak vs strong prompts |
| 2 | Role Assignment | `ChatPromptTemplate.from_messages()` |
| 3 | Few-Shot Prompting | `FewShotPromptTemplate` |
| 4 | Chain-of-Thought | Structured prompts with step-by-step framework |
| 5 | Output Format Control | JSON, Markdown, bullet templates |
| 6 | Prompt Chaining | Multi-step pipelines |
| 7 | Real-World Use Cases | Email templates, content creation |

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Activate your virtual environment and run `pip install -r requirements.txt`

2. **API Key Errors**: Ensure your `.env` file is in the lab directory (or parent) and contains a valid `OPENAI_API_KEY`

3. **Kernel not found**: In Jupyter, select the Python kernel that has your virtual environment activated

4. **Git pull conflicts**: If you have local changes, stash them first: `git stash` then `git pull`, then `git stash pop`

## Notes

- Lab 3 extends the setup from Lab 1 and Lab 2 — no additional API keys required
- API usage may incur costs depending on your usage
- Complete the exercises in the notebook to reinforce each technique
- The C-T-F-C framework (Context, Task, Format, Constraints) is the foundation for effective prompts
