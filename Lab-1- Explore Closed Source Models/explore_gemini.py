
from google import genai

from dotenv import load_dotenv

load_dotenv()
client = genai.Client()


result = client.models.generate_content(model = "gemini-2.5-flash", 
                                        contents ="Hello, how are you?")
print(result)
print("--------------------------------")
print("Response:")
print(result.text)