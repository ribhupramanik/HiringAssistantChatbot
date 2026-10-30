from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_model(messages):
    response = client.chat.completions.create(
        model="gpt-6-luna",
        messages=messages,
        temperature=1
    )
    return response.choices[0].message.content
