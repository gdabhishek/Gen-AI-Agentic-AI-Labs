# Lab 5: LLM Chat Memory (LangChain)

This lab builds on **Lab 1** (Explore Closed Source Models) through **Lab 4** (Model Parameters & Output Parsing). You'll add **conversation memory** to LangChain chatbots: stateless chains, in-memory history per session, **SQLite-backed** persistence on disk, and optional **Redis-backed** persistence (for example Redis Cloud) so history survives restarts and can be shared across processes.

## Prerequisites

- **Labs 1–4 completed** — Environment, LangChain basics, prompting, and output parsing
- Python 3.11 or higher
- API keys configured in your `.env` file (**Anthropic** required for these scripts)
- For the Redis chatbot: a **Redis** instance and connection URL (local Redis or [Redis Cloud](https://redis.io/cloud/))

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
cd "Lab-5-LLM Chat Memory - Langchain"

# Install dependencies
pip install -r requirements.txt
```

### 5. Environment Variables

Lab 5 uses **Anthropic Claude** in all chatbot scripts. Ensure your `.env` contains:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

For **`chatbot_redis_memory.py`** and **`inspect_redis_chat.py`**, also set:

```env
REDIS_URL=rediss://default:your_password@your-redis-host:port/0
```

Use **`rediss://`** when your provider requires TLS (typical for Redis Cloud). For local Redis without TLS, use `redis://localhost:6379/0`.

Optional:

```env
REDIS_KEY_PREFIX=chatbot:
REDIS_TTL_SECONDS=
```

`REDIS_KEY_PREFIX` namespaces keys if you share a database with other apps. Leave `REDIS_TTL_SECONDS` unset for no expiry; set it to a number of seconds to expire each session’s message list automatically.

## What You'll Learn

- **Stateless chat** — A simple loop with no memory (each turn is independent)
- **In-memory chat history** — `InMemoryChatMessageHistory`, `MessagesPlaceholder`, and `RunnableWithMessageHistory` with configurable `session_id`
- **Persistent memory** — `SQLChatMessageHistory` with SQLite (`conversations.db`) so history survives process restarts
- **Redis memory** — `RedisChatMessageHistory` with a Redis URL so history persists in Redis (Cloud or self-hosted)
- **Inspecting stored chats** — Reading messages from SQLite or Redis for a given session

## Usage

**Important:** Before running any script:
1. Pull the latest code: `git pull origin main`
2. Activate your virtual environment: `source venv/bin/activate`
3. Navigate to the lab directory: `cd "Lab-5-LLM Chat Memory - Langchain"`

### 1. Chatbot Without Memory (Baseline)

Each question is answered without prior context:

```bash
python chatbot_example.py
```

### 2. Chatbot With In-Memory History

Remembers the conversation for a session in RAM. Type `new_session` to switch session IDs:

```bash
python chatbot_in_memory.py
```

### 3. Chatbot With SQLite Persistent Memory

Stores chat history in `conversations.db` (created on first run):

```bash
python chatbot_persistant_memory.py
```

### 4. Inspect the SQLite Chat Database

After using the persistent chatbot, inspect stored messages for a session (default example uses `user_456`):

```bash
python inspect_sql_chat_db.py
```

### 5. Chatbot With Redis Memory

Stores chat history in **Redis** using `RedisChatMessageHistory`. Requires `REDIS_URL` in `.env`. Type `new_session` to switch session IDs (default session id is `user_redis_1`):

```bash
python chatbot_redis_memory.py
```

### 6. Inspect Redis Chat History

After using the Redis chatbot, inspect stored messages for a session (defaults match `inspect_redis_chat.py`; edit `session_id` in the script if you used another):

```bash
python inspect_redis_chat.py
```

## Project Structure

```
Lab-5-LLM Chat Memory - Langchain/
├── chatbot_example.py           # No memory — baseline REPL
├── chatbot_in_memory.py         # In-memory history + session switching
├── chatbot_persistant_memory.py # SQLite-backed SQLChatMessageHistory
├── chatbot_redis_memory.py      # Redis-backed RedisChatMessageHistory
├── inspect_sql_chat_db.py       # Read messages from conversations.db
├── inspect_redis_chat.py        # Read messages from Redis for a session
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Key Concepts

| File | Concept |
|------|---------|
| `chatbot_example.py` | `ChatPromptTemplate`, no history |
| `chatbot_in_memory.py` | `RunnableWithMessageHistory`, `InMemoryChatMessageHistory`, `MessagesPlaceholder` |
| `chatbot_persistant_memory.py` | `SQLChatMessageHistory`, SQLite `conversations.db` |
| `chatbot_redis_memory.py` | `RedisChatMessageHistory`, Redis URL from `REDIS_URL` |
| `inspect_sql_chat_db.py` | Inspecting persisted `BaseMessage` list for a session (SQLite) |
| `inspect_redis_chat.py` | Inspecting persisted `BaseMessage` list for a session (Redis) |

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError** (e.g. `langchain_community`): Run `pip install -r requirements.txt`

2. **API Key Errors**: Ensure `.env` includes a valid `ANTHROPIC_API_KEY`

3. **SQLite / connection errors**: Run `chatbot_persistant_memory.py` first so `conversations.db` exists before inspecting; adjust `session_id` in `inspect_sql_chat_db.py` if you used a different session

4. **Redis connection errors**: Confirm `REDIS_URL` matches your provider (TLS → `rediss://`). Check host, port, password, and firewall rules. Run `chatbot_redis_memory.py` at least once before inspecting; align `session_id` in `inspect_redis_chat.py` with the session you used

5. **Git pull conflicts**: If you have local changes, stash them first: `git stash` then `git pull`, then `git stash pop`

## Notes

- Lab 5 extends Labs 1–4 — you need an Anthropic API key for the provided model (`claude-sonnet-4-20250514`)
- API usage may incur costs depending on your usage
- In-memory history is lost when the process exits; SQLite and Redis keep history across restarts (Redis also supports multiple app instances talking to the same store)
- Do not commit `conversations.db` if it contains sensitive chat data — add it to `.gitignore` if needed
- Do not commit `.env` or paste Redis URLs with passwords into public repositories
