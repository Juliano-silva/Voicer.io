from selenium import webdriver
import time

def Google_Pesquisa(Voz_String,palavrasearch):
    options = webdriver.ChromeOptions()

    Palavra = str(Voz_String).lower()
    Pesquisa = Palavra.split(f"{palavrasearch}")[1]

    driver = webdriver.Chrome(options=options)

    driver.get(f"https://www.google.com/search?q={Pesquisa}")

    while True:
        time.sleep(1)