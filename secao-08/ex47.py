"""
47. Faça uma função que receba uma matriz 4x4 e retorne quantos valores maiores do que
10 ela possui.

"""

matriz = [[1, 5, 6, 12], [1, 2, 6, 3], [1, 5, 4, 20], [2, 54, 12, 4]]

def maior_10(matriz):
    cont = 0
    for l in range(4):
        for i in range(4):
            if matriz[l][i] > 10:
                cont += 1
    
    return cont

print(maior_10(matriz))
