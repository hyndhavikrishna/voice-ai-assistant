import speech_recognition as sr
from src.audio_utils import record_audio, speak
from src.llm_utils import ask_llm

def main():
    try:
        question = record_audio()
    except sr.WaitTimeoutError:
        print("[ERROR] Listening timed out.")
        return
    except Exception as e:
        print(f"[ERROR] {e}")
        return

    print("You:", question)

    # Get LLM answer (handles rate limits internally)
    answer = ask_llm(question)
    print("Bot:", answer)
    speak(answer)

if __name__ == "__main__":
    main()
