import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def redimensionar_imagem():
    caminho_imagem = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if not caminho_imagem:
        return

    try:
        largura = int(entry_largura.get())
        altura = int(entry_altura.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para largura e altura.")
        return

    # Carregar a imagem
    imagem = Image.open(caminho_imagem)
    
    # Redimensionar a imagem
    nova_imagem = imagem.resize((largura, altura))

    # Criar um novo nome para a imagem redimensionada
    caminho_nova_imagem = f"imagem_redimensionada_{largura}x{altura}.jpg"
    
    # Salvar a nova imagem
    nova_imagem.save(caminho_nova_imagem)
    
    messagebox.showinfo("Sucesso", f"Imagem redimensionada salva como: {caminho_nova_imagem}")

# Criar a janela principal
root = tk.Tk()
root.title("Redimensionador de Imagens")

# Criar os elementos da interface
label_largura = tk.Label(root, text="Largura:")
label_largura.pack(pady=5)

entry_largura = tk.Entry(root)
entry_largura.pack(pady=5)

label_altura = tk.Label(root, text="Altura:")
label_altura.pack(pady=5)

entry_altura = tk.Entry(root)
entry_altura.pack(pady=5)

btn_redimensionar = tk.Button(root, text="Selecionar Imagem e Redimensionar", command=redimensionar_imagem)
btn_redimensionar.pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
