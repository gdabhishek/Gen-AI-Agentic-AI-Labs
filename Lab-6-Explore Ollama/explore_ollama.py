#Install ollama -- pip install langchain-ollama==1.0.0 in local environment

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


llm = init_chat_model(
    model="llama3.1:8b",  # Specify the Ollama model to use
    model_provider="ollama",         
    base_url="https://YOUR_NGROK_URL.ngrok-free.app"  #Paste the ngrok url here
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "What is the capital of France?")
])

chain = prompt | llm

response = chain.invoke({"input": "What is the capital of France?"})
print(response)
print("-"*100)
print(response.content)