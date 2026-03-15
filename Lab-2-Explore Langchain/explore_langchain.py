from langchain_core.prompts import PromptTemplate

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM    
llm = init_chat_model("claude-haiku-4-5-20251001", model_provider="anthropic")

# Create the prompt
prompt = PromptTemplate.from_template(
    """
    You are a customer service agent. Take this customer complaint,
    analyze the sentiment, categorize the issue, suggest a solution,
    and write a professional response. Also check our knowledge base
    and escalate if needed...
    {issue}
    """
)

# Create and run chain
#| -- pipeline operator
chain = prompt | llm  #chain
response = chain.invoke({"issue": "I'm having trouble with my account"})
print(response)
print("---------------")
print(response.content)
