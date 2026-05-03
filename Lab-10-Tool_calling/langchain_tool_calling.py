from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, SearchApiAPIWrapper
import os
import requests
from dotenv import load_dotenv

from datetime import datetime
load_dotenv()

LLM_MODEL = "gpt-5-mini"

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

search = SearchApiAPIWrapper()

@tool
def get_weather(city: str) -> str:
    """
    Retrieve current weather information for a specified city using the OpenWeatherMap API.

    Args:
        city (str): The name of the city to query.

    Returns:
        str: Weather data as a JSON string or an error message.
    """
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return "Error: OPENWEATHER_API_KEY environment variable not set."
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return f"Error: Could not fetch weather data. Status code: {response.status_code}"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

@tool
def get_disk_space(path: str = None) -> str:

    """
    Get disk space information for a given path. If no path is provided, uses the current working directory. Returns total, used, and free space in GB.

    Args:
        path (str): The path to get disk space information for. If not provided, uses the current working directory.

    Returns:
        str: Disk space information as a string.
    """
    if path in ["", None]:
        path = os.getcwd()  # Use current working directory as default
    
    try:
        stat = os.statvfs(path)
        total = (stat.f_blocks * stat.f_frsize) / (1024**3)  # Convert to GB
        free = (stat.f_bavail * stat.f_frsize) / (1024**3)  # Fixed: was stat.bavail, should be stat.f_bavail
        used = total - free
        return f"Disk space for {path}: Total: {total:.2f} GB, Used: {used:.2f} GB, Free: {free:.2f} GB"
    except Exception as e:
        return f"Error getting disk space: {str(e)}"

@tool
def get_current_date_and_time() -> str:
    """
    Get the current date and time in the format of YYYY-MM-DD HH:MM:SS.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def search_tool(query: str) -> str:
    """
    Search the web for the given query.

    Args:
        query (str): The query to search the web for.

    Returns:
        str: The search results.
    """
    return search.run(query)


tools = [get_weather, get_disk_space, search_tool, wikipedia, get_current_date_and_time]

llm = ChatOpenAI(model=LLM_MODEL)

llm_with_tools = llm.bind_tools(tools)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to various tools. Use the tools when needed to provide accurate information."),
    ("human", "{user_input}")
])


def execute_tool_calls_and_continue(messages, llm_with_tools):
    """Execute tool calls and continue the conversation."""
    
    last_message = messages[-1]
    print(last_message.tool_calls)
    if last_message.tool_calls:
        # Map tool names to their handlers
        tool_handlers = {
            "get_weather": lambda args: get_weather.invoke(input=args),
            "get_disk_space": lambda args: get_disk_space.invoke(input=args),
            "search_tool": lambda args: search_tool.invoke(args["query"]),
            "wikipedia": lambda args: wikipedia.invoke(args["query"]),
            "get_current_date_and_time": lambda args: get_current_date_and_time.invoke(input=args)

        }
        
        for tool_call in last_message.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            
            # Execute the appropriate tool
            if tool_name in tool_handlers:
                print(f"Executing {tool_name} tool...")
                result = tool_handlers[tool_name](tool_args)
            else:
                result = f"Unknown tool: {tool_name}"
            
            # Add tool result to conversation
            tool_message = ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )
            messages.append(tool_message)
        
        # Continue the conversation with tool results
        response = llm_with_tools.invoke(messages)
        messages.append(response)

        if response.tool_calls:
            return execute_tool_calls_and_continue(messages, llm_with_tools)
        else:
            return response
        
    else:
        return last_message

def chat_with_tools(user_input: str) -> str:
    """Complete chat flow with tool execution."""
    
    # Format the prompt template with user input
    messages = chat_prompt.format_messages(user_input=user_input)
    
    response = llm_with_tools.invoke(messages)
    messages.append(response)
    
    # Execute tools if needed and continue
    final_response = execute_tool_calls_and_continue(messages, llm_with_tools)
    
    return final_response.content

while True:
    user_question = input("You: ")
    if user_question in ["quit","exit"]:
        break

    response = chat_with_tools(user_question)
    print("Bot :", response)