import os
from dotenv import load_dotenv

# 1) Load .env if it exists (puts OPENAI_API_KEY into os.environ)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

# 2) Check for a key
api_key = os.getenv("OPENAI_API_KEY")
DEMO = not api_key  # if no key, we’re in demo mode

# 3) Only import OpenAI when in real mode
if not DEMO:
    from openai import OpenAI, OpenAIError
    client = OpenAI(api_key=api_key)

def ask_llm(prompt: str) -> str:
    if DEMO:
        # Demo mode: just echo back your prompt
        return f"[Demo] You said: {prompt}"

    # Real mode: call the API and handle errors
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.choices[0].message.content.strip()
    except OpenAIError:
        return "Sorry, I’m unavailable right now—please try again later."
