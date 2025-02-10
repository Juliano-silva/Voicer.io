import threading
import time

import speech_recognition as sr

r = sr.Recognizer()
e = threading.Event()

with sr.Microphone() as source:
    audio = r.listen(source)
    Falar = r.recognize_google(audio, language="pt-BR")

    print(Falar)
e.set()