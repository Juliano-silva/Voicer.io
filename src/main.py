from flask import * 
import webview,os,sys,sqlite3
import YggDrasil

app = Flask(__name__)
webview.create_window("FileWizard",app,width=500,height=750)
Banco = r"C:\Users\sustu\Pictures\Programmation\Projeto Principais\FileWizard\src\BancoDados.db"

@app.route("/",methods=["GET","POST"])
def Home():
    return render_template("index.html")

@app.route("/YggDrasil",methods=["GET","POST"])
def Ygg():
    YggDrasil.Chamar("C:/")
    return "",205

@app.route("/Voice",methods=["GET","POST"])
def Voices():
    data = request.get_json()
    ComandoVoz = str(data["Voz"]).lower()
    for i in range(0,YggDrasil.Row_Length()):
        Arquivo_Name = str(YggDrasil.All_respostas("name",i)).lower().split(".")[0]
        if ComandoVoz == f"abrir {Arquivo_Name}":
            os.startfile(fr"{YggDrasil.All_respostas("arquivo",i)}")
    if ComandoVoz == "abrir google":
        os.startfile(r"C:\Users\sustu\AppData\Local\Programs\Opera GX\opera.exe")
    elif ComandoVoz == "fechar google":
        os.system(r"taskkill /f /im opera.exe")
    elif ComandoVoz == "abrir steam":
        os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")
    elif ComandoVoz == "fechar steam":
        os.system(r"taskkill /f /im steam.exe")
    else:
        print("Fechar")
    return "",205

if __name__ == "__main__":
    webview.start(debug=True,http_port=2506)