# Simple Text Summarizer using Ollama
# Install ollama -- pip install langchain-ollama in local environment

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


# Initialize the LLM with Ollama
llm = init_chat_model(
    model="llama3.1:8b",  # Specify the Ollama model to use                
    model_provider="ollama",         
    base_url="https://YOUR_NGROK_URL.ngrok-free.app"  # Paste the ngrok url here
)

# Enhanced prompt template with detailed persona and instructions
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert content analyst and summarization specialist with years of experience 
in distilling complex information into clear, concise summaries. Your role is to:

INSTRUCTIONS:
1. Read the entire text carefully to understand the full context
2. Identify the main topic, key points, and supporting details
3. Preserve the original meaning and intent of the author
4. Focus on facts, conclusions, and important insights
5. Maintain logical flow and coherence in your summary
6. Use clear, professional language appropriate to the content
7. Avoid adding information not present in the original text
8. Do not include personal opinions or interpretations beyond what's stated

OUTPUT FORMAT:
- Write 2-3 well-structured sentences
- Start with the main topic or central idea
- Include the most important supporting points
- End with any key conclusions or implications if relevant
- Use proper grammar and punctuation
- Be concise but comprehensive"""),
    
    ("user", """Please provide a high-quality summary of the following text. 
Follow all the guidelines provided and ensure accuracy and clarity.

TEXT TO SUMMARIZE:
{text}

Now provide your summary:""")
])

# Create the chain
chain = prompt | llm

# Example text to summarize (you can replace this with any text)
sample_text = """
Artificial Intelligence (AI) has revolutionized many industries in recent years. 
Machine learning algorithms can now process vast amounts of data and identify patterns 
that humans might miss. In healthcare, AI is being used to diagnose diseases, predict 
patient outcomes, and assist in drug discovery. In finance, it helps detect fraud and 
make trading decisions. Autonomous vehicles use AI to navigate roads safely. 
Natural language processing enables chatbots and virtual assistants to understand 
and respond to human language. Despite these advances, there are concerns about job 
displacement, privacy, and the ethical implications of AI decisions. As AI continues 
to evolve, it will likely become even more integrated into our daily lives.
"""

# Invoke the chain
response = chain.invoke({"text": sample_text})

# Display results
print("=" * 100)
print("ORIGINAL TEXT:")
print("=" * 100)
print(sample_text)
print("\n" + "=" * 100)
print("SUMMARY:")
print("=" * 100)
print(response.content)
print("=" * 100)