from flask import *
import time,re
from static.Bibliotecas.GoogleAbrir import Google_Pesquisa

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def Home():
    return render_template("index.html")


@app.route("/Main_Microfone",methods=["GET","POST"])
def Microfone():
    data = request.get_json()
    Voz_String = str(f"{data["Value"]}").lower()

    if re.search("pesquisa",Voz_String) and re.search("fim",Voz_String):
        Google_Pesquisa(Voz_String,"pesquisa")

    return "",205


if __name__ == "__main__":
    app.run(debug=True,port=5252)