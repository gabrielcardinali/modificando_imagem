import imagens

# Este programa aplica algumas transformadas geométricas simples em uma imagem.

# Ler o arquivo 'jardim.jpg' e o mostrar na tela
im1 = imagens.Imagem('cores.jpg')
im1.mostrar()

# Pegar o número de linhas (altura) e número de colunas (largura)
# da matriz que representa a imagem
m = im1.altura
n = im1.largura

# Criar uma imagem im2 "vazia", colorida, de tamanho m x n
im2 = imagens.Imagem('', (m, n))

# Produzir imagem rotacionada em 180°
for i in range(0, m):
    for j in range(0, n):
        im2[i][j] = im1[m-i-1][n-j-1]
im2.mostrar()

# -------------------------------------------------------------------
# INSERIR SEU CÓDIGO ABAIXO DESTA LINHA

# Produzir imagem espelhada na horizontal
im2 = imagens.Imagem('', (m, n))
for i in range(0, m):
    for j in range(0, n):
        im2[i][j] = im1[i][n-j-1]
im2.mostrar()

# Produzir imagem espelhada na vertical
im2 = imagens.Imagem('', (m, n))
for i in range(0, m):
    for j in range(0, n):
        im2[i][j] = im1[m-i-1][j]
im2.mostrar()

# Produzir imagem transposta
im2 = imagens.Imagem('', (n, m))
for i in range(0, m):
    for j in range(0, n):
        im2[j][i] = im1[i][j]
im2.mostrar()

# Produzir imagem rotacionada 90° no sentido horário
im2 = imagens.Imagem('', (n, m))
for i in range(0, m):
    for j in range(0, n):
        im2[j][i] = im1[m-i-1][j]
im2.mostrar()

# Produzir imagem rotacionada 90° no sentido anti-horário
im2 = imagens.Imagem('', (n, m))
for i in range(0, m):
    for j in range(0, n):
        im2[j][i] = im1[i][n-j-1]
im2.mostrar()
