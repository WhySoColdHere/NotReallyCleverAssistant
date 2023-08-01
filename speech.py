import pyttsx3

engine = pyttsx3.init()


def speech_text(text):
    engine.say(text)
    engine.runAndWait()


