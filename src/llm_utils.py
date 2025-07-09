import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load .env into os.environ
load_dotenv()

# 2. Create the client with your key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return resp.choices[0].message.content.strip()
