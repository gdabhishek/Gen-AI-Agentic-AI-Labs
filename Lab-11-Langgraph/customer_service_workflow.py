from langgraph.graph import StateGraph, START, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from dotenv import load_dotenv

load_dotenv()

# Updated model to gpt-5-mini
llm = init_chat_model("gpt-5-mini", model_provider="openai")

llm_validator = init_chat_model("gpt-4.1", model_provider="openai")

 
#state
class CS_State(TypedDict):
    message: str
    sentiment: str
    category: str
    response :str
    validation: str
    validator_reasoning: str


def sentiment_analysis(state):
    print("Analysing sentiment of the customer message")
    message = state["message"]
    sentiment_prompt = ChatPromptTemplate.from_template(
            "Analyze the sentiment of this customer message: {message}\n"
            "Respond with only: positive, neutral, or negative"
        )
    sentiment_chain = sentiment_prompt | llm | StrOutputParser()
    sentiment = sentiment_chain.invoke({"message": message})
    return {"sentiment": sentiment}


def category_analysis(state):
    print("Analysing category of the customer message")
    message = state["message"]
    category_prompt = ChatPromptTemplate.from_template(
        "Categorize this customer issue: {message}\n"
        "Categories: billing, technical, product, shipping\n"
        "Respond with only the category name."
    )
    category_chain = category_prompt | llm | StrOutputParser()
    category = category_chain.invoke({"message": message})
    return {"category": category}


def response_generation(state):
    print("Generating response to the customer message")
    message = state["message"]
    sentiment = state["sentiment"]
    category = state["category"]
    if "validation" in state and state["validation"]=="no":
        print("Generating response to the customer message with validation")
        response = state["response"]
        reasoning = state["validator_reasoning"]
        response_prompt = ChatPromptTemplate.from_template(
            '''The previous response to the customer message was found to be invalid. 
                Here is the resoning of the validator for your previous response
                {reasoning}
            
            Please generate a new, improved response to the following customer message: {message}\nPrevious response: {response}\n"
            "Sentiment: {sentiment}\n"
            "Category: {category}\n"
            "Be helpful and empathetic.'''
        )
        response_chain = response_prompt | llm | StrOutputParser()
        response = response_chain.invoke({"message": message, "sentiment": sentiment, "category": category, "response": response,"reasoning":reasoning})
    else:
        response_prompt = ChatPromptTemplate.from_template(
            "Generate a response to this customer message: {message}\n"
            "Sentiment: {sentiment}\n"
            "Category: {category}\n"
            "Be helpful and empathetic."
        )
        response_chain = response_prompt | llm | StrOutputParser()
        response = response_chain.invoke({"message": message, "sentiment": sentiment, "category": category})
    return {"response": response}

def validate_response(state):
    print("Validating the response to the customer message")
    message = state["message"]
    response = state["response"]

    validate_prompt = ChatPromptTemplate.from_template(
        '''You are an expert evaluator. Review the following AI-generated customer service response for helpfulness, empathy, and completeness. Does the response fully address the customer's message in a helpful and empathetic manner, with sufficient information? Respond in a JSON foramt with validation and reasoning

        Format:
        {{"validation":"yes/no", "validator_reasoning":""}}
 

        Customer message: {message}
        AI-generated response: {response}
        '''
        
    )
    

    validate_chain = validate_prompt | llm_validator | JsonOutputParser()
    validation = validate_chain.invoke({"message": message, "response": response})
    print(f"Validation: {validation}")
    return validation


#Langgraph graph


#Initialize the graph
cs_workflow = StateGraph(CS_State)

#Add Nodes to the graph
cs_workflow.add_node("sentiment_analysis", sentiment_analysis)
cs_workflow.add_node("category_analysis", category_analysis)
cs_workflow.add_node("response_generation", response_generation)
cs_workflow.add_node("validate_response", validate_response)



def route_after_validation(state):
    if state["validation"] == "no":
        print("Response :",  state["response"])
        return "response_generation"
    else:
        return "end"
#Add the edges to connect the nodes
cs_workflow.add_edge(START, "sentiment_analysis")
cs_workflow.add_edge("sentiment_analysis", "category_analysis")
cs_workflow.add_edge("category_analysis", "response_generation")
cs_workflow.add_edge("response_generation", "validate_response")
cs_workflow.add_conditional_edges(
    "validate_response", 
    route_after_validation,
    {"end": END, "response_generation": "response_generation"}
)


#Compile the workflow
cs_workflow = cs_workflow.compile()
cs_workflow.get_graph().draw_mermaid_png(output_file_path="customer_service_workflow.png")


user_input = {"message": "My order is late and I'm really frustrated!"}
result = cs_workflow.invoke(user_input)

print("Result :", result)
