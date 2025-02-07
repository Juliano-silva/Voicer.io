def Executar(nome):
    return f"Olá,Mundo sou {nome}"

def Comandos(Comando_Voz,Comando_Aceitavel,Comando_Def):
    if str(Comando_Voz).lower() == str(Comando_Aceitavel).lower():
        resultado = Comando_Def("Juliano")
        print(resultado)
    else:
        print("Não Aceito")
    

Comandos("Cachorro","Cachorro",Executar)