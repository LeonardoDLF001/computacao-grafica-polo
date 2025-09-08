import os
from PIL import Image

# Pasta origem com as imagens
folder_path = "metades"

# Pasta destino para salvar as imagens recortadas
output_folder = "metades_recortadas"

# Cria a pasta destino se não existir
os.makedirs(output_folder, exist_ok=True)

# Largura da borda a ser cortada (em pixels)
border_width = 25

# Percorre todos os arquivos na pasta origem
for filename in os.listdir(folder_path):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        filepath = os.path.join(folder_path, filename)
        img = Image.open(filepath)
        width, height = img.size

        if filename.endswith("_esquerda.png") or filename.endswith("_esquerda.jpg") or filename.endswith("_esquerda.jpeg"):
            # Corta 25 pixels da borda direita
            cropped_img = img.crop((0, 0, width - border_width, height))
            print(f"Cortando 23 pixels da borda direita da imagem {filename}")

        elif filename.endswith("_direita.png") or filename.endswith("_direita.jpg") or filename.endswith("_direita.jpeg"):
            # Corta 25 pixels da borda esquerda
            cropped_img = img.crop((border_width, 0, width, height))
            print(f"Cortando 23 pixels da borda esquerda da imagem {filename}")

        else:
            continue

        # Salva a imagem recortada na pasta destino
        output_path = os.path.join(output_folder, filename)
        cropped_img.save(output_path)