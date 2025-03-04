import os,sys,time,sqlite3,random,json

Banco = sqlite3.connect("Banco.db")
Cursor = Banco.cursor()

Cursor.execute(""" CREATE TABLE IF NOT EXISTS Historico 
               (id INTEGER  PRIMARY key AUTOINCREMENT,Path BLOB,File TEXT) """)

def Return_List():
    return Cursor.execute(f"SELECT * FROM Historico")

def Retorn_Historico(Id):
    return Cursor.execute(f"SELECT File FROM Historico where id={Id}")

def Open_File():
    # os.startfile(f"{Retorn_Historico(2,2)}")
    

def YggDrasil(files):
    for dirpath,dirname,filename in os.walk("C:/"):
        for file in filename:
            if file in files:
                print("Arquivo Localizado")
                Path_Full = os.path.join(dirpath,file)
                Cursor.execute(f"""INSERT INTO Historico values (
                               NULL,
                               "{str(file)}",
                               "{str(Path_Full)}"
                               )""")
                Banco.commit()
                sys.exit()
# YggDrasil("Algebra linear.pdf")
Open_File()