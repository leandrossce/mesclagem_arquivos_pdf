import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def search_and_merge_pdfs(nome1, nome2, dir1, dir2):
    nome1_lower = nome1.lower()
    nome2_lower = nome2.lower()

    def search_pdfs(nome1, nome2, directory):
        pdf_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.pdf') and nome1 in file.lower() and nome2 in file.lower():
                    pdf_files.append(os.path.join(root, file))
        return pdf_files

    pdf_files_dir1 = search_pdfs(nome1_lower, nome2_lower, dir1)
    pdf_files_dir2 = search_pdfs(nome1_lower, nome2_lower, dir2)
    pdf_files = pdf_files_dir1 + pdf_files_dir2

    if not pdf_files:
        messagebox.showinfo("Informação", f"Nenhum arquivo PDF contendo '{nome1}' e '{nome2}' foi encontrado nos diretórios fornecidos.")
        return

    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    first_pdf_nome = os.path.splitext(os.path.basename(pdf_files[0]))[0].upper()
    output_filenome = os.path.join(r"C:\Users\Gabriel\Downloads", f"{first_pdf_nome}.pdf")
    
    merger.write(output_filenome)
    merger.close()

    

def select_csv_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    csv_file_var.set(filepath)

def select_dir1():
    directory = filedialog.askdirectory()
    dir1_var.set(directory)

def select_dir2():
    directory = filedialog.askdirectory()
    dir2_var.set(directory)

def start_merge():
    csv_file = csv_file_var.get()
    nome2 = nome2_var.get()
    dir1 = dir1_var.get()
    dir2 = dir2_var.get()

    if not all([csv_file, nome2, dir1, dir2]):
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
        return

    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for line in reader:
            nome1 = line[0]
            search_and_merge_pdfs(nome1, nome2, dir1, dir2)
    
    messagebox.showinfo("Alerta", f"Fim!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Mesclagem")

csv_file_var = tk.StringVar()
nome2_var = tk.StringVar()
dir1_var = tk.StringVar()
dir2_var = tk.StringVar()

# Layout da GUI
tk.Label(root, text="Caminho do arquivo CSV:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=csv_file_var, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Selecionar", command=select_csv_file).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Nome 2:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=nome2_var, width=50).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Diretório 1:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=dir1_var, width=50).grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Selecionar", command=select_dir1).grid(row=2, column=2, padx=10, pady=5)

tk.Label(root, text="Diretório 2:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=dir2_var, width=50).grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Selecionar", command=select_dir2).grid(row=3, column=2, padx=10, pady=5)

tk.Button(root, text="Iniciar Mesclagem", command=start_merge).grid(row=4, column=0, columnspan=3, pady=20)

root.mainloop()
