from PIL import Image
import os

input_folder = "recortadas"
output_folder = "metades"

os.makedirs(output_folder, exist_ok=True)

print(f"Cortando imagens da pasta '{input_folder}' ao meio...")

for nome_arquivo in sorted(os.listdir(input_folder)):
    if nome_arquivo.lower().endswith(".png"):
        caminho_entrada = os.path.join(input_folder, nome_arquivo)
        imagem = Image.open(caminho_entrada)

        largura, altura = imagem.size
        meio = largura // 2

        esquerda = imagem.crop((0, 0, meio, altura))
        esquerda_filename = os.path.join(output_folder, f"{os.path.splitext(nome_arquivo)[0]}_esquerda.png")
        esquerda.save(esquerda_filename)

        direita = imagem.crop((meio, 0, largura, altura))
        direita_filename = os.path.join(output_folder, f"{os.path.splitext(nome_arquivo)[0]}_direita.png")
        direita.save(direita_filename)

        print(f"{nome_arquivo} cortada ao meio -> {esquerda_filename}, {direita_filename}")

print(f"\nProcesso concluído! Metades salvas na pasta '{output_folder}'.")