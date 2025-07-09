import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv

load_dotenv()  # loads the OPENAI_API_KEY from .env

def ask_llm(prompt: str) -> str:
    resp = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}])
    return resp.choices[0].message.content.strip()

