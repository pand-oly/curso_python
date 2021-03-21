"""
4. Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do
maior valor.

"""

matriz = [[1, 5, 6, 3], [5, 8, 7, 5], [6, 5, 4, 51], [25, 4, 8, 4]]
maior = matriz[0][0]
for l in range(0, 4):
    for c in range(0, 4):
        if matriz[l][c] > maior:
            maior = matriz[l][c]
            IndexLinha = matriz.index(matriz[l])
            IndexColuna = matriz.index(matriz[c])
            
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]}]', end='')
    print()


print(f'Maior número é {maior} que se encontra na posição [{IndexLinha},{IndexColuna}]')