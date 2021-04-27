"""
51. Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule e retorne a soma
dos elementos que estão na diagonal secundária.

"""

matriz = [[1, 2, 4], [1, 2, 3], [4, 2, 3]]
def calculo(matriz):
    soma = 0
    for l in range(0, 3):
        matriz[l] = matriz[l][::-1]
        for c in range(0, 3):
            if l == c:
                soma += matriz[c][l]

    return soma

print(calculo(matriz))
