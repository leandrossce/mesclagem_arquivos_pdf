import os
import pandas as pd
from PyPDF2 import PdfMerger
import csv

def search_and_merge_pdfs(nome1, nome2, dir1, dir2):
    # Converter os nomes para minúsculas para garantir a pesquisa insensível a maiúsculas/minúsculas
    nome1_lower = nome1.lower()
    nome2_lower = nome2.lower()

    # Função para buscar arquivos PDF recursivamente em um diretório
    def search_pdfs(nome1, nome2, directory):
        pdf_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.pdf') and nome1 in file.lower() and nome2 in file.lower():
                    pdf_files.append(os.path.join(root, file))
        return pdf_files

    # Buscar os arquivos PDF nos diretórios fornecidos de forma recursiva
    pdf_files_dir1 = search_pdfs(nome1_lower, nome2_lower, dir1)
    pdf_files_dir2 = search_pdfs(nome1_lower, nome2_lower, dir2)

    # Combinar os resultados das buscas nos dois diretórios
    pdf_files = pdf_files_dir1 + pdf_files_dir2

    # Verificar se foram encontrados arquivos
    if not pdf_files:
        print(f"Nenhum arquivo PDF contendo '{nome1}' e '{nome2}' foi encontrado nos diretórios fornecidos.")
        return

    # Mesclar os arquivos PDF encontrados
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    # Nome do arquivo resultante da mesclagem
    first_pdf_nome = os.path.splitext(os.path.basename(pdf_files[0]))[0].upper()
    output_filenome = os.path.join(r"C:\Users\Gabriel\Downloads", f"{first_pdf_nome}.pdf")
    
    merger.write(output_filenome)
    merger.close()

    print(f"Arquivos mesclados com sucesso em '{output_filenome}'")

if __name__ == "__main__":

    csv_file = "C:\\Users\\Gabriel\\Downloads\\teste1\\arquivos.csv"

    nome2="-082024"

    dir1='C:\\Users\\Gabriel\\Downloads\\teste\\'
    dir2='C:\\Users\\Gabriel\\Downloads\\teste1\\'   

    # Abrir o arquivo CSV e iterar sobre cada linha
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        
        i = 0

        for line in reader:
            
            nome1=line[0]


            search_and_merge_pdfs(nome1, nome2, dir1, dir2)
