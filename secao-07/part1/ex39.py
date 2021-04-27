"""
39. Escreva um programa que leia um número inteiro positivo n e em seguida impriman linhas do
chamado Triangulo de Pascal:

1
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1


! Revisar depois que aprender melhor sobre 'def'
"""

def calcula_posicao(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return int(calcula_posicao(n - 1, k - 1)) + int(calcula_posicao(n - 1, k))


def pascalLine(linhas):
    linhas = linhas + 1
    triangulo = []

    for linha in range(linhas):
        valores_linha = []

        for coluna in range(linha + 1):
            valores_linha.append(calcula_posicao(linha, coluna))

        triangulo.append(valores_linha)

    return triangulo

for l in range(0, 6):
    print(pascalLine(5)[l])