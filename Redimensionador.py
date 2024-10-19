import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def redimensionar_imagem():
    global imagem  # Tornar a imagem global para manter a referência

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

    # Escolher local de salvamento
    caminho_nova_imagem = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("BMP files", "*.bmp")])
    if not caminho_nova_imagem:
        return
    
    # Salvar a nova imagem
    nova_imagem.save(caminho_nova_imagem, quality=int(entry_quality.get()) if entry_quality.get() else 100)
    
    messagebox.showinfo("Sucesso", f"Imagem redimensionada salva como: {caminho_nova_imagem}")

def visualizar_imagem():
    caminho_imagem = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if not caminho_imagem:
        return

    # Carregar a imagem
    imagem_original = Image.open(caminho_imagem)
    imagem_original.thumbnail((300, 300))  # Reduzir a imagem para visualização
    img_tk = ImageTk.PhotoImage(imagem_original)

    # Exibir a imagem
    label_visualizacao.config(image=img_tk)
    label_visualizacao.image = img_tk  # Manter uma referência à imagem

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

label_quality = tk.Label(root, text="Qualidade (1-100):")
label_quality.pack(pady=5)
entry_quality = tk.Entry(root)
entry_quality.pack(pady=5)

btn_visualizar = tk.Button(root, text="Selecionar Imagem para Visualização", command=visualizar_imagem)
btn_visualizar.pack(pady=5)

label_visualizacao = tk.Label(root)
label_visualizacao.pack(pady=5)

btn_redimensionar = tk.Button(root, text="Selecionar Imagem e Redimensionar", command=redimensionar_imagem)
btn_redimensionar.pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
