"""
23. Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto
escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o
produto escalar, sendo que o produto escalar é dado por: xı * yı + x2 * y2 + ... + Xn * Yn.

"""

x = []
y = []
for v in range(0, 5):
    num = int(input('Informe valor de x: '))
    x.append(num)

for v in range(0, 5):
    num = int(input('Informe valor de y: '))
    y.append(num)


xy = 0
for i in range(0, 3):
    xy += x[i] * y[i]

print('Vetor X: ', x)
print('Vetor Y: ', y)
print('Produto escalar: ', xy)
