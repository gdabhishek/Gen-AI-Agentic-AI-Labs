from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model #LLM as plug and play model
from dotenv import load_dotenv
load_dotenv()

# Initialize the LLM    
llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# Create the prompt
prompt = PromptTemplate.from_template(
    """
    You are a customer service agent. Take this customer complaint,
    analyze the sentiment, categorize the issue, suggest a solution,
    and write a professional response. Also check our knowledge base
    and escalate if needed...

    Complaint:
    {issue}
    """
)

# Create and run chain
#| -- pipeline operator
chain = prompt | llm | StrOutputParser()  #chain

response = chain.invoke({"issue": "I'm having trouble with my account"})
print(response)

