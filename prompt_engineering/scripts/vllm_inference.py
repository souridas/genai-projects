from openai import OpenAI
from openai.types.shared import responses_model
from pydantic import BaseModel
import instructor
import outlines
''' nohup vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0 --api-key souridas510 & 
USE THE ABOVE COMMAND TO START THE SERVER

'''
client = OpenAI(
    base_url="http://0.0.0.0:8000/v1",api_key="souridas510"
)
client = instructor.from_openai(client)
class User(BaseModel):
    name: str
    age: int
    hobbies: list[str]
    job: str

messages = [
    {
        "role": "user",
        "content": "create a user."
    }
]

response = client.chat.completions.create(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    messages=messages,
    response_model=User
)

print(response)  # Print the response                