"""
7. Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da forma:

A[i[j] = 2i + 7j - 2 se i < j; 
A[i][j] = 3i² - 1 se i = j; 
A[i][j] = 4i³ - 5j² +1 se i > j.

"""

matriz = [[], [], [], [], [], [], [], [], [], []]
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            cal = (2 * i) + (7 * j) - 2
        elif i == j:
            cal = (3 * i **2) - 1 
        else:
            i > j
            cal = (4 * i **3) - (5 * j **2) +1
        matriz[i].append(cal)

for l in range(0, 10):
    for c in range(0, 10):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()
