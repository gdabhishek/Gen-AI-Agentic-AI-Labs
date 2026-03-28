"""Print stored messages for a session using the same Redis settings as chatbot_redis_memory.py."""

import os

from dotenv import load_dotenv
from langchain_community.chat_message_histories import RedisChatMessageHistory

load_dotenv()


def retrieve_redis_history(
    session_id: str = "user_redis_1",
    *,
    url: str | None = None,
    key_prefix: str | None = None,
):
    redis_url = url or os.environ.get("REDIS_URL")
    if not redis_url:
        raise SystemExit("Set REDIS_URL in your environment or .env file.")

    prefix = key_prefix if key_prefix is not None else os.environ.get(
        "REDIS_KEY_PREFIX", "chatbot:"
    )

    history = RedisChatMessageHistory(
        session_id=session_id,
        url=redis_url,
        key_prefix=prefix,
    )
    messages = history.messages
    print(f"Retrieved {len(messages)} messages for session: {session_id}")
    return messages


if __name__ == "__main__":
    messages = retrieve_redis_history(session_id="user_redis_1")
    print(messages)
    for i, message in enumerate(messages):
        print(f"Message {i + 1}: {type(message).__name__} - {message.content}")
