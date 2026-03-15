from anthropic import Anthropic

from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

# models_list = client.models.list()
# print(models_list)
# for model in models_list:
#     print(model.display_name, model.id)
prompt = "Hello, How are you today?"
message = client.messages.create(
    model="claude-sonnet-4-6",  # Current Claude Sonnet 4
    max_tokens=1024,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(message)
print("--------------------------------")
print("Response:")
print(message.content[0].text)