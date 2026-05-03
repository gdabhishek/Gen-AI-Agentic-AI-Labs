import openai
from typing import Dict, Any
import json
import inspect
import os
import requests
from dotenv import load_dotenv

load_dotenv()

LLM_MODEL = "gpt-5-mini"


#Custome tool


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


# Convert to OpenAI tool format
def convert_to_openai_tool(func):
    """Convert a Python function to OpenAI tool format."""
    
    sig = inspect.signature(func)
    params = {}
    required = []
    
    for name, param in sig.parameters.items():
        param_type = param.annotation
        if param_type == str:
            params[name] = {"type": "string"}
        elif param_type == float:
            params[name] = {"type": "number"}
        elif param_type == int:
            params[name] = {"type": "integer"}
        elif param_type == bool:
            params[name] = {"type": "boolean"}
        
        if param.default == inspect.Parameter.empty:
            required.append(name)
    
    return {
        "type": "function",
        "function": {
            "name": func.__name__,
            "description": func.__doc__,
            "parameters": {
                "type": "object",
                "properties": params,
                "required": required
            }
        }
    }


tools = [
    convert_to_openai_tool(get_weather),
    convert_to_openai_tool(get_disk_space),
]


def call_openai_with_tools(user_message: str) -> Dict[str, Any]:
    """Call OpenAI with tool calling enabled."""
    
    response = openai.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": user_message}],
        tools=tools,
        tool_choice="auto"  # Let AI decide when to use tools
    )
    
    return response.choices[0].message

user_message = "What is AI ?"

ai_response = call_openai_with_tools(user_message)
print("AI Response:", ai_response)

def execute_tool_calls(message: Dict[str, Any]) -> list:
    """Execute the tool calls from the AI response and return tool messages."""
    
    tool_messages = []
    
    # Check if message has tool_calls (new format)
    if "tool_calls" in message and message["tool_calls"]:
        # Map function names to actual functions
        function_map = {
            "get_weather": get_weather,
            "get_disk_space": get_disk_space
        }
        
        # Execute each tool call
        for tool_call in message["tool_calls"]:
            func_name = tool_call["function"]["name"]
            arguments = json.loads(tool_call["function"]["arguments"])
            tool_call_id = tool_call["id"]
            
            if func_name not in function_map:
                result = f"Unknown function: {func_name}"
            else:
                # Execute the function
                try:
                    result = function_map[func_name](**arguments)

                except Exception as e:
                    result = f"Error executing {func_name}: {str(e)}"
            
            # Create tool message with tool_call_id
            tool_messages.append({
                "role": "tool",
                "tool_call_id": tool_call_id,
                "content": str(result)
            })
    
    return tool_messages
ai_response = ai_response.model_dump()  # convert to dictionary
if ai_response.get("tool_calls"):
    tool_messages = execute_tool_calls(ai_response)
    print("Tool output:", tool_messages)
    print("--------------------------------")
    # Step 3: Send result back to AI for final answer
    messages = [
        {"role": "user", "content": user_message},
        ai_response,
    ]
    messages.extend(tool_messages)
    
    final_response = openai.chat.completions.create(
        model=LLM_MODEL,
        messages=messages
    )
    
    print("Final Response:", final_response.choices[0].message.content)
    print("--------------------------------")
else:
    print(ai_response.get("content", "No content in response"))