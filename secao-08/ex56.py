"""
56. Faça uma função que recebe, por parâmetro, uma matriz A[7][6] e uma linha N e retorne
a soma dos elementos dessa linha.

"""

matriz = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 
[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

def calculo(matriz, n):
    soma = sum(matriz[n])

    return soma

n = int(input('Digite valor de n: '))

print(calculo(matriz, n))
