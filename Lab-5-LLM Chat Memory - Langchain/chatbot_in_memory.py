from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

_sessions = {}

llm = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")

def get_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in _sessions:
        _sessions[session_id] = InMemoryChatMessageHistory()
    return _sessions[session_id]

def get_chain_with_history():
    
    
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Remember user details."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}")
    ])
    
    chain = prompt | llm
    
    
    # Wrap the chain with history
    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_history,
        input_messages_key="question",
        history_messages_key="chat_history",
        
    )
    
    return chain_with_history
    

config = {"configurable": {"session_id": "user_123"}} 
chain = get_chain_with_history()
while True:
    message  = input("You: ")
    if message.lower() == "new_session":
        config["configurable"]["session_id"] = input("Enter new session id: ")
        chain = get_chain_with_history()
        continue
    

    response = chain.invoke(
        {"question": message},
        config=config
    )
    print("Assistant: ", response.content)