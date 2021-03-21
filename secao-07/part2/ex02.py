"""
2. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e 0 como os demais
elementos. Escreva ao final a matriz obtida.

"""

matriz = [[], [], [], [], []]

for l in range(0, 5):
    for c in range(0, 5):
        if l == c:
            n = 1
            matriz[l].append(n)
        else:
            n = 0
            matriz[l].append(n)

for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]}]', end='')
    print()
