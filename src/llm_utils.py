import os
from dotenv import load_dotenv
from openai import OpenAI, error as openai_error

# Load the .env file in the project root
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENAI_API_KEY in environment")

# Instantiate the new-style client
client = OpenAI(api_key=api_key)

def ask_llm(prompt: str) -> str:
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.choices[0].message.content.strip()
    except openai_error.RateLimitError:
        return "Sorry, I’m out of capacity right now — please try again later."


