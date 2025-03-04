import os,sys,time,sqlite3,random

Banco = sqlite3.connect("Banco.db")
Cursor = Banco.cursor()

Cursor.execute(""" CREATE TABLE IF NOT EXISTS Historico (id INT,Path BLOB,File TEXT) """)

def YggDrasil(files):
    for dirpath,dirname,filename in os.walk("C:/"):
        for file in filename:
            if file in files:
                print("Arquivo Localizado")
                Path_Full = os.path.join(dirpath,file)
                Cursor.execute(f"""INSERT INTO Historico values (
                               67,
                               "{str(file)}",
                               "{str(Path_Full)}"
                               )""")
                sys.exit()

Banco.commit()

YggDrasil("opera.exe")