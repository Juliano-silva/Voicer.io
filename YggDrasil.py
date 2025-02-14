import os,sqlite3
from pathlib import Path
from colorist import *



def YggDrasil(URL,File):
    Banco = sqlite3.connect(File)
    cursor = Banco.cursor()
    URL_ATUAL = os.listdir(URL)
    cursor.execute("""CREATE TABLE IF NOT EXISTS History (id INTEGER PRIMARY key AUTOINCREMENT,name TEXT,arquivo ou Pasta BLOB)""")
    
    while True:
        if os.path.isfile(URL) == True:
            break
        else:
            for i in range(0,len(os.listdir(URL))):
                if os.path.isfile(f"{URL}{URL_ATUAL[i]}") == True:
                    print(f"{Color.RED}[{i}] - {URL_ATUAL[i]} - Arquivo{Color.OFF}")
                else:
                    print(f"{Color.BLUE}[{i}] - {URL_ATUAL[i]} - Pasta{Color.OFF}")

        Escolha = int(input("Faça sua Escolha: "))

        if os.path.isfile(f"{URL}{URL_ATUAL[Escolha]}") == True:
            URL += URL_ATUAL[Escolha]
            FILE_OPEN = str(rf"{URL}").replace("/","\\")
            cursor.execute(f'INSERT INTO History values(null,"{str(FILE_OPEN).split("\\")[-1]}","{FILE_OPEN}")')

            extension = str(FILE_OPEN).split(".")[1]

            if extension == "py":
                os.system(f"python {FILE_OPEN}")
            elif extension == "js":
                os.system(f"node {FILE_OPEN}")
            elif extension == "java":
                os.system(f"java {FILE_OPEN}")
            else:
                os.startfile(FILE_OPEN)
        else:
            URL += URL_ATUAL[Escolha] + "/"
            URL_ATUAL = os.listdir(URL)

    Banco.commit()

YggDrasil("C:/","BancoDados.db")