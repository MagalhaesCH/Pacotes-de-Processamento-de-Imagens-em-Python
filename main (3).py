install opencv-python
install Pillow
install scikit-image

import cv2

# Carregar imagem
imagem = cv2.imread('imagem_exemplo.jpg')

# Exibir imagem
cv2.imshow('Imagem', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

from PIL import Image

# Carregar imagem
imagem = Image.open('imagem_exemplo.jpg')

# Exibir imagem
imagem.show()

from skimage import io

# Carregar imagem
imagem = io.imread('imagem_exemplo.jpg')

# Exibir imagem
io.imshow(imagem)
io.show()

from skimage import io

# Carregar imagem
imagem = io.imread('imagem_exemplo.jpg')

# Exibir imagem
io.imshow(imagem)
io.show()

# Converter imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagem Cinza', imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()

from skimage.color import rgb2gray

# Converter imagem para escala de cinza
imagem_cinza = rgb2gray(imagem)
io.imshow(imagem_cinza)
io.show()

# Redimensionar imagem
imagem_redimensionada = cv2.resize(imagem, (200, 200))
cv2.imshow('Imagem Redimensionada', imagem_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Redimensionar imagem
imagem_redimensionada = imagem.resize((200, 200))
imagem_redimensionada.show()

from skimage.transform import resize

# Redimensionar imagem
imagem_redimensionada = resize(imagem, (200, 200))
io.imshow(imagem_redimensionada)
io.show()

# Rotacionar imagem
(h, w) = imagem.shape[:2]
centro = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(centro, 45, 1.0)
imagem_rotacionada = cv2.warpAffine(imagem, M, (w, h))
cv2.imshow('Imagem Rotacionada', imagem_rotacionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
