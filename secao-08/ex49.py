"""
49. Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule e retorne a soma
dos elementos que estão abaixo da diagonal principal.

"""

matriz = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
def calculo(matriz):
    soma = 0
    for l in range(0, 3):
        for c in range(0, 3):
            if l < c:
                soma += matriz[c][l]
    return soma

print(calculo(matriz))
