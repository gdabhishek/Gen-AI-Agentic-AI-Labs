

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

def get_sentiment(x):
    return x["sentiment"]

def get_category(x):
    return x["category"]

def get_message(x):
    return x["message"]

# Run sentiment and category in parallel, then generate response
parallel_chain = (
    RunnableParallel(
        {
            "message": get_message,  # Pass through the original message
            "sentiment": sentiment_chain,
            "category": category_chain
        }
    )
    |  {  
        "sentiment":get_sentiment,   
        "category": get_category,
        "response": response_chain
        }
)

#with lambda function
# parallel_chain = (
#     RunnableParallel(
#         {
#             "message": get_message,  # Pass through the original message
#             "sentiment": sentiment_chain,
#             "category": category_chain
#         }
#     )
#     | {  
#         "sentiment":lambda x: x["sentiment"],   
#         "category": lambda x: x["category"],
#         "response": response_chain
#         }
# )

result = parallel_chain.invoke({"message": "I love your product but the shipping was slow"})
print(f"\nFinal Response:\n{result}")

