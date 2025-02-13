import os,sqlite3
# Pegar a URL inicial e Adicionar 

def YggDrasil():
    Banco = sqlite3.connect("BancoDados.db")
    cursor = Banco.cursor()
    URL_Add = "/"
    URL_ATUAL = os.listdir(URL_Add)
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS History (
               id INTEGER PRIMARY key AUTOINCREMENT,
               name TEXT,
               arquivo ou Pasta BLOB)""")
    
    while True:
        if os.path.isfile(URL_Add) == True:
            break
        else:
            for i in range(0,len(os.listdir(URL_Add))):
                if os.path.isfile(f"{URL_Add}{URL_ATUAL[i]}") == True:
                    print(f"[{i}] - {URL_ATUAL[i]} - Arquivo")
                elif os.path.isdir(f"{URL_Add}{URL_ATUAL[i]}") == True:
                    print(f"[{i}] - {URL_ATUAL[i]} - Pasta")
                else:
                    print("Outro Tipo de Arquivo")

        Escolha = int(input("Faça sua Escolha: "))

        if os.path.isfile(f"{URL_Add}{URL_ATUAL[Escolha]}") == True:
            URL_Add += URL_ATUAL[Escolha]
            FILE_OPEN = str(rf"{URL_Add}").replace("/","\\")
            cursor.execute(f'INSERT INTO History values(null,"{FILE_OPEN}","{FILE_OPEN}")')
            os.startfile(FILE_OPEN)
        else:
            URL_Add += URL_ATUAL[Escolha] + "/"
            URL_ATUAL = os.listdir(URL_Add)

    Banco.commit()