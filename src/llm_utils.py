import os
from dotenv import load_dotenv

# Load .env if present (puts OPENAI_API_KEY into env)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

# Grab the key (may be None)
api_key = os.getenv("OPENAI_API_KEY")

# If there's no API key, we're in demo mode
DEMO = not api_key

if not DEMO:
    from openai import OpenAI, OpenAIError
    client = OpenAI(api_key=api_key)

def ask_llm(prompt: str) -> str:
    if DEMO:
        # Simple echo when no key
        return f"[Demo] You said: {prompt}"

    # Real API call (with a friendly catch-all)
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.choices[0].message.content.strip()
    except OpenAIError:
        return "Sorry, I’m unavailable right now—please try again later."
