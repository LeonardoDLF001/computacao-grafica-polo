import os
from PIL import Image
import re

input_folder = "metades_recortadas"
output_folder = "imagens_concatenadas"
os.makedirs(output_folder, exist_ok=True)

files = os.listdir(input_folder)
esquerda_files = [f for f in files if f.endswith("_esquerda.png")]

# Função para extrair o número do nome do arquivo para ordenar corretamente
def extrair_numero(nome_arquivo):
    # Exemplo: "pagina_enem_2_esquerda.png" -> extrai 2
    match = re.search(r'_(\d+)_esquerda\.png$', nome_arquivo)
    if match:
        return int(match.group(1))
    else:
        return -1  # Caso não encontre número, coloca no início

# Ordena os arquivos pela numeração extraída
esquerda_files.sort(key=extrair_numero)

imagens_concatenadas = []

for esquerda_file in esquerda_files:
    numero = extrair_numero(esquerda_file)
    if numero == -1:
        continue  # pula arquivos sem número válido

    # Limite para parar na página 27
    if numero > 27:
        break

    base_name = esquerda_file.replace("_esquerda.png", "")
    direita_file = base_name + "_direita.png"

    esquerda_path = os.path.join(input_folder, esquerda_file)
    direita_path = os.path.join(input_folder, direita_file)

    if os.path.exists(direita_path):
        img_esquerda = Image.open(esquerda_path)
        img_direita = Image.open(direita_path)

        largura = max(img_esquerda.width, img_direita.width)
        altura = img_esquerda.height + img_direita.height

        nova_img = Image.new("RGBA", (largura, altura))
        nova_img.paste(img_esquerda, (0, 0))
        nova_img.paste(img_direita, (0, img_esquerda.height))

        imagens_concatenadas.append(nova_img)
    else:
        print(f"Arquivo correspondente não encontrado para: {esquerda_file}")

if imagens_concatenadas:
    largura_final = max(img.width for img in imagens_concatenadas)
    altura_final = sum(img.height for img in imagens_concatenadas)

    imagem_final = Image.new("RGBA", (largura_final, altura_final))

    y_offset = 0
    for img in imagens_concatenadas:
        imagem_final.paste(img, (0, y_offset))
        y_offset += img.height

    output_path = os.path.join(output_folder, "todas_concatenadas.png")
    imagem_final.save(output_path)
    print(f"Imagem final com todas as imagens concatenadas salva em: {output_path}")
else:
    print("Nenhuma imagem concatenada foi criada.")
