"""
10. Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão na diagonal
principal.

"""

matriz = [[4, 5, 6], [4, 5, 6], [4, 5, 6]]
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        if l == c:
            soma += matriz[c][l]

print(soma)