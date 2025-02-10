# Teste 1

# import speech_recognition as sr

# reconhecedor = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Diga algo:")
#     audio = reconhecedor.listen(source,1)
    


# Falar = reconhecedor.recognize_google(audio, language="pt-BR")


# print(Falar)

# Teste 2
import threading
import time

import speech_recognition as sr


def inside_code():

    e = threading.Event()

    def f1():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source, 2)
            Falar = r.recognize_google(audio, language="pt-BR")
            print(Falar)
        e.set()

    def f2():
        TimeLeft = 2

        while not e.is_set() and TimeLeft != 0:
            print(f'You have {TimeLeft} seconds left.')
            time.sleep(1)
            TimeLeft -= 1
    
    thread_list = [threading.Thread(target=f1), threading.Thread(target=f2)]
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


inside_code()