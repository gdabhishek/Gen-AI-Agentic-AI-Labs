from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()
import os

llm = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")

prompt =  ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant, who answers user questions"),
    ("user", "{question}")
])


chain = prompt | llm  #chain
while True:
    question = input("You: ")
    response = chain.invoke({"question": question})
    print("Bot: ", response.content)