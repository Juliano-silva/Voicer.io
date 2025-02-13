import os
from PIL import Image
# Pegar a URL inicial e Adicionar 

# "/Reproduction_Folder/music/"


URL_Add = "/"
URL_ATUAL = os.listdir(URL_Add)

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
        imagem = Image.open(f"{URL_Add}")
        imagem.show()
    else:
        URL_Add += URL_ATUAL[Escolha] + "/"
        URL_ATUAL = os.listdir(URL_Add)
    