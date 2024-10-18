from PIL import Image

# Carregar a imagem
imagem = Image.open("OIP.jpg")

# Redimensionar a imagem
nova_imagem = imagem.resize((1920, 1080))


nova_imagem.save("imagem_redimensionada4.jpg")
