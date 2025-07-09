import os
from dotenv import load_dotenv
from openai import OpenAI

# 1) Load .env into os.environ
load_dotenv()

# 2) Read the key (and error out early if it’s missing)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENAI_API_KEY in environment")

# 3) Create the client with that key
client = OpenAI(api_key=api_key)

def ask_llm(prompt: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message.content.strip()

