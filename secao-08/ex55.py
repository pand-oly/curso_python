"""
55. Faça uma função que recebe, por parâmetro, uma matriz A[3][3] e retorna a soma dos
elementos da sua diagonal principal e da sua diagonal secundária

"""

matriz = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
def calculo(matriz):
    soma = 0
    for l in range(3):
        for c in range(3):
            if l == c:
                soma += matriz[c][l]
    
    for l in range(3):
        matriz[l] = matriz[l][::-1]
        for c in range(3):
            if l == c:
                soma += matriz[c][l]

    return soma

print(calculo(matriz))
