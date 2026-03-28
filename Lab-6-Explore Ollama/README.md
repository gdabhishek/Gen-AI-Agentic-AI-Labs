# Lab 6: Explore Ollama

This lab builds on **Lab 1** through **Lab 5**. You’ll run **open models locally** (or via a tunneled server) using **Ollama** and **LangChain**—no cloud LLM API keys required when Ollama is running on your machine.

## Prerequisites

- **Labs 1–5 completed** — Comfortable with Python, virtual environments, and LangChain chains
- Python 3.11 or higher
- **Ollama** installed and running, *or* a reachable Ollama API URL (for example from [Google Colab + ngrok](COLAB_SETUP_GUIDE.md))

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

```bash
# If you're currently in the lab folder, go up one directory:
cd ..

# Or navigate from the project root:
# cd "/path/to/Gen-AI-Agentic-AI-Labs"
```

### 3. Activate Virtual Environment

```bash
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 4. Navigate to the Lab Directory and Install Dependencies

```bash
cd "Lab-6-Explore Ollama"

pip install -r requirements.txt
```

### 5. Run Ollama and Pull a Model

**Option A — Local Ollama (recommended for your laptop)**

1. Install Ollama from [ollama.com](https://ollama.com) and start it (it usually listens on `http://localhost:11434`).
2. Pull the model used in the scripts (or adjust the model name in code):

```bash
ollama pull llama3.1:8b
```

**Option B — Ollama in Google Colab + ngrok**

Follow **[COLAB_SETUP_GUIDE.md](COLAB_SETUP_GUIDE.md)** to run `Ollama_Serving.ipynb`, expose port `11434` with ngrok, and copy the public `https://…ngrok-free.app` URL.

### 6. Configure `base_url` in the Python Scripts

The sample scripts use a placeholder **ngrok** URL. Update **`base_url`** in each script:

- **Local Ollama:** set to `http://localhost:11434` (or omit `base_url` if your LangChain/Ollama defaults match your setup).
- **Remote (ngrok):** paste your current ngrok URL from the Colab notebook output.

Files to edit: `explore_ollama.py`, `Text_summarizer.py`.

## What You'll Learn

- **LangChain + Ollama** — `init_chat_model(..., model_provider="ollama")` with a local or remote `base_url`
- **Simple chain** — `ChatPromptTemplate` piped to an Ollama-backed chat model
- **Text summarization** — A longer system prompt and structured user message for summarizing arbitrary text
- **Serving Ollama from Colab** — Install Ollama, tunnel with ngrok, run models on GPU (see notebook and Colab guide)

## Usage

**Important:** Before running:
1. Pull the latest code: `git pull origin main`
2. Activate your virtual environment
3. Ensure Ollama is running and the model is pulled (or your ngrok URL is valid)
4. Set `base_url` in the scripts as described above

### Run the Basic Ollama Example

```bash
python explore_ollama.py
```

### Run the Text Summarizer

```bash
python Text_summarizer.py
```

### Run the Colab Serving Notebook

Open **`Ollama_Serving.ipynb`** in Jupyter or upload it to [Google Colab](https://colab.research.google.com/). Step-by-step instructions are in **[COLAB_SETUP_GUIDE.md](COLAB_SETUP_GUIDE.md)**.

## Project Structure

```
Lab-6-Explore Ollama/
├── explore_ollama.py          # Minimal LangChain + Ollama chain
├── Text_summarizer.py         # Summarization with a detailed system prompt
├── Ollama_Serving.ipynb       # Colab: install Ollama, ngrok, serve models
├── COLAB_SETUP_GUIDE.md       # Detailed Colab + ngrok walkthrough
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Key Concepts

| Resource | Topic |
|----------|--------|
| `explore_ollama.py` | `model_provider="ollama"`, `base_url`, `llama3.1:8b` |
| `Text_summarizer.py` | Long-form system prompt, `{text}` placeholder, summarization chain |
| `Ollama_Serving.ipynb` | Ollama install on Colab, ngrok tunnel to port `11434` |
| `COLAB_SETUP_GUIDE.md` | ngrok authtoken, finding the public URL, troubleshooting |

## Troubleshooting

### Common Issues

1. **Connection refused / cannot reach Ollama** — Confirm Ollama is running (`ollama serve` or the desktop app) and `base_url` matches (often `http://localhost:11434`).

2. **Model not found** — Run `ollama pull llama3.1:8b` or change the `model=` string in the script to a model you have installed (`ollama list`).

3. **ModuleNotFoundError** — Run `pip install -r requirements.txt` inside your activated virtual environment.

4. **ngrok URL stopped working** — Free ngrok URLs change when the tunnel restarts; copy the new URL from the notebook output and update your Python scripts.

5. **Git pull conflicts** — Stash local changes: `git stash`, then `git pull`, then `git stash pop`.

## Notes

- Lab 6 does **not** require OpenAI/Anthropic keys for the Ollama path; runs are limited by your hardware and Ollama’s license terms for each model.
- Colab sessions are ephemeral; ngrok URLs and GPU time are subject to Colab and ngrok free-tier limits—see **COLAB_SETUP_GUIDE.md**.
- The notebook may pull a different model (e.g. `gemma3:12b`); align the `model` name in your local scripts with what is actually served if you mix Colab and local clients.
