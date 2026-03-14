from anthropic import Anthropic

from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",  # Current Claude Sonnet 4
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, How are you today?"}
    ]
)

print(message)
print("--------------------------------")
print("Response:")
print(message.content[0].text)