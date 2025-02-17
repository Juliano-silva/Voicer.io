import os,sqlite3,json
from pathlib import Path
from colorist import *

Dados = r"C:\Users\sustu\Pictures\Programmation\Projeto Principais\FileWizard\src\BancoDados.db"
conection = sqlite3.connect(Dados,check_same_thread=False)
cursor = conection.cursor()
cursor.execute(f"SELECT * FROM History")
rows_Length = cursor.fetchall()


Lista_Extensão = '''{
    "Extension":[
        {"Sigla":"py","Comando":"python"},
        {"Sigla":"js","Comando":"node"},
        {"Sigla":"java","Comando":"java"}
    ]
    }'''

def Chamar(URL):
    URL_ATUAL = os.listdir(URL)
    cursor.execute("""CREATE TABLE IF NOT EXISTS History (id INTEGER PRIMARY key AUTOINCREMENT,name TEXT,arquivo ou Pasta BLOB)""")
    cursor.execute("""   delete from History where rowid not in
                   (select min(rowid) from History
                   group by arquivo
                   ); """)
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
            Comandos = json.loads(Lista_Extensão)["Extension"]
            for Comand in Comandos:
                if extension == Comand["Sigla"]:
                    os.system(Comand["Comando"] + " " + FILE_OPEN)
                else:
                    os.startfile(FILE_OPEN)
        else:
            URL += URL_ATUAL[Escolha] + "/"
            URL_ATUAL = os.listdir(URL)

       
    conection.commit()


def Buscar(Escolha,index):
    cursor.execute(f"SELECT {Escolha} FROM History")
    rows = cursor.fetchall()
    return rows[index]

def All_respostas(columname,index): return Buscar(f"{columname}",index)[0]
def Row_Length(): return len(rows_Length)

def Remover():
    cursor.execute(""" DROP TABLE History """)

    conection.commit()