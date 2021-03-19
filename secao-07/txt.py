
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


print(pascalLine(5))