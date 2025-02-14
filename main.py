import time,threading
import speech_recognition as sr
import YggDrasil

r = sr.Recognizer()
e = threading.Event()

def Executar(nome):
    return f"Olá,Mundo sou {nome} Falou"

def Comandos(Comando_Voz,Comando_Aceitavel,Comando_Def):
    if str(Comando_Voz).lower() == str(Comando_Aceitavel).lower():
        resultado = Comando_Def("Juliano")
        print(resultado)
    else:
        print("Não Aceito")


with sr.Microphone() as source:
    audio = r.listen(source)
    Falar = r.recognize_google(audio, language="pt-BR")

    print(Falar)
    Comandos(f"{Falar}","Cachorro",Executar)
e.set()