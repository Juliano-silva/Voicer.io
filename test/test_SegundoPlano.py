from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

# Função para criar uma imagem para o ícone
def create_image(width, height, color1, color2):
    image = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(image)
    draw.rectangle(
        (width // 4, height // 4, width * 3 // 4, height * 3 // 4),
        fill=color2
    )
    return image

# Funções para o menu
def on_clicked(icon, item):
    print(f"Você clicou em: {item.text}")

# Criar o menu
menu = Menu(
    MenuItem('Opção 1', lambda icon, item: on_clicked(icon, item)),
    MenuItem('Sair', lambda icon, item: icon.stop())
)

# Criar o ícone
icon = Icon(
    "Meu Ícone",
    create_image(64, 64, 'blue', 'white'),
    menu=menu
)

# Executar o ícone
icon.run()