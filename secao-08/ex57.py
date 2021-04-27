"""
57. Faça uma função que recebe, por parâmetro, uma matriz A[7][6] e uma coluna N e retorne
a soma dos elementos dessa coluna.

"""

matriz = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 
[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

def calculo(matriz, n):
    soma = 0
    for l in range(7):
        soma += matriz[l][n]

    return soma

n = int(input('Digite valor de n: '))

print(calculo(matriz, n))
