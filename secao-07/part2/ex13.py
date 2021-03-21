"""
13. Gere matriz 4 x 4 com valores no intervalo [1, 20). Escreva um programa que transforme a
matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os elementos
acima da diagonal principal. Imprima a matriz original e a matriz transformada.

"""

matriz = [[4, 5, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7]]
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]}]', end='')
    print()
print()
nova = matriz.copy()
for l in range(0, 4):
    for c in range(0, 4):
        if l > c:
            nova[c][l] *= 0

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]}]', end='')
    print()
