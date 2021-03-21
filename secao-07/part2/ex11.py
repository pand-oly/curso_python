"""
11. Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão na diago
nal secundária.

"""

matriz = [[4, 5, 4], [4, 5, 6], [4, 5, 6]]
soma = 0
for l in range(0, 3):
    matriz[l] = matriz[l][::-1]
    for c in range(0, 3):
        if l == c:
            soma += matriz[c][l]
    matriz[l] = matriz[l][::-1]

print(soma)

# 0  1  2
#[4, 5, 6] 0 | 0 2
#[4, 5, 6] 1 | 1 1
#[4, 5, 6] 2 | 2 0
