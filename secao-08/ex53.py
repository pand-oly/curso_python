"""
53. Faça uma função que verifica se uma matriz quadrada de ordem N é a matriz identidade.

"""

matriz = [[1, 2, 3, 4], [6, 1, 3, 4], [6, 2, 1, 4], [6, 2, 3, 1]]

def identidade(matriz):
    for l in range(4):
        for c in range(4):
            if l == c:
                if matriz[l][c] == 1:
                    var = 'É uma matriz identidade'
                else:
                    var = 'Não é uma matriz identidade'
                    return var
    return var

print(identidade(matriz))
