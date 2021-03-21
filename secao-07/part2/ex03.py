"""
3. Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linha e da
coluna de cada elemento. Em seguida, imprima na tela a matriz.

"""

matriz = [[], [], [], []]
for l in range(0, 4):
    for c in range(0, 4):
        valor = l * c
        matriz[l].append(valor)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]}]', end='')
    print()
