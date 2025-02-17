import sqlite3,json
Banco = r"C:\Users\sustu\Pictures\Programmation\Projeto Principais\FileWizard\src\BancoDados.db"
conection = sqlite3.connect(Banco)
cursor = conection.cursor()
cursor.execute(f"SELECT * FROM History")
rows_Length = cursor.fetchall()


def Buscar(Escolha,index):
    cursor.execute(f"SELECT {Escolha} FROM History")
    rows = cursor.fetchall()
    return rows[index]


for i in range(0,len(rows_Length)):
    print(Buscar("name",i)[0])