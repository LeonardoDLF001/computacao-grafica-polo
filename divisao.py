from pdf2image import convert_from_path
import os

pdf_path = "enem2024.pdf"
output_folder = "imagens"

if not os.path.exists(output_folder): 
    os.makedirs(output_folder)

resolucao_dpi = 300

print (f"Convertendo '{pdf_path}' para imahgens com {resolucao_dpi} DPI...")