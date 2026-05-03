# Lab 12: Tool Calling with OpenAI and LangChain

This lab demonstrates how to implement function/tool calling with OpenAI models using both the OpenAI SDK directly and LangChain framework. The examples show how to create custom tools and integrate them with language models.

## Overview

This lab contains two implementations:
1. **`openai_tool_call.py`** - Direct OpenAI API implementation for tool calling
2. **`langchain_tool_calling.py`** - LangChain-based implementation with additional tools (DuckDuckGo search, Wikipedia)


## Setup Instructions

### 1. Install Dependencies

First, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Get an OpenWeather API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to the [API Keys section](https://home.openweathermap.org/api_keys)
4. Copy your API key (it may take a few minutes to activate)

**Note**: The free tier allows 60 calls per minute, which is sufficient for testing.

``` in .env
OPENWEATHER_API_KEY=your_openweather_api_key_here
```
