"""
6. Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posição
das matrizes lidas.

"""

matriz1 = [[], [], [], []]
for l in range(0, 4):
    for c in range(0, 4):
        num = int(input(f'Preencha a primeira matriz digite posição [{l}, {c}]: '))
        matriz1[l].append(num)

matriz2 = [[], [], [], []]
for l in range(0, 4):
    for c in range(0, 4):
        num = int(input(f'Preencha a segunda matriz digite posição [{l}, {c}]: '))
        matriz2[l].append(num)

print('')
print('-=' * 30)
print('')
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz1[l][c]:^4}]', end='')
    print()

print('')
print('-=' * 30)
print('')
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz2[l][c]:^4}]', end='')
    print()

matriz3 = [[], [], [], []]
for l in range(0, 4):
    for c in range(0, 4):
        if matriz1[l][c] >= matriz2[l][c]:
            matriz3[l].append(matriz1[l][c])
        else: 
            matriz2[l][c] > matriz1[l][c]
            matriz3[l].append(matriz2[l][c])

print('')
print('-=' * 30)
print('')
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz3[l][c]:^4}]', end='')
    print()
