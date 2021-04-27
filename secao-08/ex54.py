"""
54. Faça uma função que recebe, por parâmetro, uma matriz A[4][4] e retorna a soma dos
seus elementos.

"""

matriz = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
def calculo(matriz):
    soma = 0
    for l in range(4):
       soma += sum(matriz[l])
 
    return soma

print(calculo(matriz))
