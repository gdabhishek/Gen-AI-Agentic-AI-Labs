#Explore OpenAI library

from openai import OpenAI #Class for interacting with the OpenAI API
from dotenv import load_dotenv

load_dotenv()
#Initialize the OpenAI client instance
client = OpenAI()

#Define the prompt
prompt = "Hi, How are you?"

response = client.chat.completions.create(
    model = "gpt-5.1",
    messages = [{"role": "user", "content": prompt}]
)

print(response)
print("--------------------------------")
print("Response:")
#Print the response
print(response.choices[0].message.content)
