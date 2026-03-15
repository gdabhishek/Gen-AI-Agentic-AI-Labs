

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

# Step 1: Sentiment Analysis Chain
sentiment_prompt = PromptTemplate.from_template(
    "Analyze sentiment of: {message}\n"
    "Respond with only: positive, neutral, or negative"
)
sentiment_chain = sentiment_prompt | llm | StrOutputParser()

# Step 2: Category Classification Chain  
category_prompt = PromptTemplate.from_template(
    "Categorize this issue: {message}\n"
    "Categories: billing, technical, product, shipping\n"
    "Respond with only the category."
)
category_chain = category_prompt | llm | StrOutputParser()

# Step 3: Response Generation Chain
response_prompt = PromptTemplate.from_template(
    """Write a professional customer service response.
    
Original message: {message}
Sentiment: {sentiment}
Category: {category}

Be helpful and empathetic."""
)
response_chain = response_prompt | llm | StrOutputParser()

full_chain = (
    RunnablePassthrough.assign(sentiment=sentiment_chain) 
    | RunnablePassthrough.assign(category=category_chain) 
    | response_chain
)


result = full_chain.invoke({"message": "My order is late and I'm really frustrated!"})


print(f"\nFinal Response:\n{result}")
