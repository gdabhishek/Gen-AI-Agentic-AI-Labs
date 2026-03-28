from langchain_community.chat_message_histories import SQLChatMessageHistory

def retrieve_sql_history(session_id="test_session", db_path="test.db"):
    """
    Retrieve chat history from SQL database
    
    Args:
        session_id (str): The session ID to retrieve history for
        db_path (str): Path to the SQLite database file
    
    Returns:
        list: List of chat messages for the session
    """
    # Create SQL history instance
    sql_history = SQLChatMessageHistory(
        session_id=session_id,
        connection_string=f"sqlite:///{db_path}"
    )
    
    # Retrieve and return messages
    messages = sql_history.messages
    print(f"Retrieved {len(messages)} messages for session: {session_id}")
    
    return messages


if __name__ == "__main__":
    messages = retrieve_sql_history(session_id="user_456", db_path="conversations.db")
    print(messages)
    for i, message in enumerate(messages):
        print(f"Message {i+1}: {type(message).__name__} - {message.content}") 