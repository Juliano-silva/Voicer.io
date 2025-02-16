import time,threading,os
import speech_recognition as sr
import src.YggDrasil as YggDrasil

r = sr.Recognizer()
e = threading.Event()

def Comandos(Comando_Voz):
    Comando_Voz = str(Comando_Voz).lower()
    if Comando_Voz in str("opera").lower():
        os.startfile(r"C:\Users\sustu\AppData\Local\Programs\Opera GX\opera.exe")
    elif Comando_Voz in str("steam").lower():
        os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")
    else:
        print("Nada")

# YggDrasil("C:/Users/sustu/Pictures/Test/","BancoDados.db")
with sr.Microphone() as source:
    audio = r.listen(source)
    Falar = r.recognize_google(audio, language="pt-BR")

    print(Falar)
    Comandos(f"{Falar}")
e.set()