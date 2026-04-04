from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()
# import os
# REDIS_URL = os.environ.get("REDIS_URL")
# print(REDIS_URL)

import os
import redis

url = os.environ.get("REDIS_URL")


# Connect to Redis
r = redis.Redis(
    host='<host>',
    port=15502,
    decode_responses=True,
    username="default",
    password="<password>",
)

r.delete("chatbot:user_redis_1")