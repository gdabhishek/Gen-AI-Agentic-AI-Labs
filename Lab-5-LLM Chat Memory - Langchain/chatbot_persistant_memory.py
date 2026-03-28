#Run 
# pip install langchain-community==0.4.1

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")

def get_sql_history(session_id: str) -> BaseChatMessageHistory:
    return SQLChatMessageHistory(
        session_id=session_id,
        connection="sqlite:///conversations.db"
    )

def get_chain_with_history():
    
    
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Remember user details."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])
    
    chain = prompt | llm

    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_sql_history,
        input_messages_key="input",
        history_messages_key="chat_history"
    )
    
    return chain_with_history
    
    
config = {"configurable": {"session_id": "user_456"}} 
chain = get_chain_with_history()
while True:
    message  = input("You: ")

    response1 = chain.invoke(
        {"input": message},
        config=config
    )
    print("Bot: ", response1.content)