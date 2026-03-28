import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

REDIS_URL = os.environ.get("REDIS_URL")
# Optional: isolate keys from other apps on the same database (default matches inspect_redis_chat.py)
REDIS_KEY_PREFIX = os.environ.get("REDIS_KEY_PREFIX", "chatbot:")
# Optional: expire session lists after N seconds (omit for no expiry)
_redis_ttl = os.environ.get("REDIS_TTL_SECONDS")


def _ttl_seconds() -> int | None:
    if _redis_ttl is None or _redis_ttl.strip() == "":
        return None
    return int(_redis_ttl)


if not REDIS_URL:
    raise SystemExit(
        "Missing REDIS_URL. Add it to your .env file.\n"
        "Examples:\n"
        "  Redis Cloud (TLS): rediss://default:PASSWORD@HOST:PORT/0\n"
        "  Local:             redis://localhost:6379/0\n"
    )

llm = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")


def get_redis_history(session_id: str) -> BaseChatMessageHistory:
    return RedisChatMessageHistory(
        session_id=session_id,
        url=REDIS_URL,
        key_prefix=REDIS_KEY_PREFIX,
        ttl=_ttl_seconds(),
    )


def get_chain_with_history():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Remember user details."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm

    return RunnableWithMessageHistory(
        chain,
        get_redis_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )


config = {"configurable": {"session_id": "user_redis_1"}}
chain = get_chain_with_history()
while True:
    message = input("You: ")
    if message.lower() == "new_session":
        config["configurable"]["session_id"] = input("Enter new session id: ")
        chain = get_chain_with_history()
        continue

    response = chain.invoke({"input": message}, config=config)
    print("Bot: ", response.content)
