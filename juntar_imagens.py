import os
from PIL import Image

input_folder = "metades_recortadas"
output_folder = "imagens_concatenadas"

paginas = [29, 30, 31]
imagens_concatenadas = []

# Primeiro, cria as imagens concatenadas (esquerda em cima, direita embaixo)
for pagina in paginas:
    img_esquerda_path = os.path.join(input_folder, f"pagina_enem_{pagina}_esquerda.png")
    img_direita_path = os.path.join(input_folder, f"pagina_enem_{pagina}_direita.png")
    
    img_esquerda = Image.open(img_esquerda_path)
    img_direita = Image.open(img_direita_path)
    
    largura_max = max(img_esquerda.width, img_direita.width)
    altura_total = img_esquerda.height + img_direita.height
    
    nova_img = Image.new('RGB', (largura_max, altura_total), (255, 255, 255))
    nova_img.paste(img_esquerda, (0, 0))
    nova_img.paste(img_direita, (0, img_esquerda.height))
    
    caminho_salvar = os.path.join(output_folder, f"pagina_{pagina}_concatenada.png")
    nova_img.save(caminho_salvar)
    
    imagens_concatenadas.append(nova_img)

# Agora, junta as três imagens concatenadas verticalmente
largura_final = max(img.width for img in imagens_concatenadas)
altura_final = sum(img.height for img in imagens_concatenadas)

imagem_final = Image.new('RGB', (largura_final, altura_final), (255, 255, 255))

y_offset = 0
for img in imagens_concatenadas:
    imagem_final.paste(img, (0, y_offset))
    y_offset += img.height

# Salva a imagem final com todas as páginas juntas
imagem_final.save(os.path.join(output_folder, "paginas_29_30_31_concatenadas.png"))

print("Imagem final com as páginas 29, 30 e 31 concatenadas verticalmente criada com sucesso.")