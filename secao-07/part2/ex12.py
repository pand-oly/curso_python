"""
12. Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transposta.

"""

matriz = [[4, 5, 6], [4, 5, 6], [4, 5, 6]]
transposta = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        if l == l:
            transposta[l].append(matriz[c][l])

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()
print('\n')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{transposta[l][c]}]', end='')
    print()
