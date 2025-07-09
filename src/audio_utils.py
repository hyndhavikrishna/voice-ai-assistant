import speech_recognition as sr
import pyttsx3

def record_audio(timeout=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("[⏺️] Listening…")
        audio = recognizer.listen(mic, timeout=timeout)
    return recognizer.recognize_google(audio)

def speak(text: str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


