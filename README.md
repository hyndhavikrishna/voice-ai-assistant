# Voice AI Assistant

A minimal CLI voice assistant that records your question, sends it to OpenAI’s Chat API, and replies via text-to-speech.

## Setup

```bash
# 1. Clone repo & enter folder
git clone https://github.com/your-username/voice-ai-assistant.git
cd voice-ai-assistant

# 2. Create & activate venv
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Secure your API key
echo "OPENAI_API_KEY=sk-<your_key_here>" > .env
