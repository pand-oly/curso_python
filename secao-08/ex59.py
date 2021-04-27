"""
59. Faça uma função que recebe, por parâmetro, 2 vetores de 10 elementos inteiros e que
calcule e retorne, também por parâmetro, o vetor união dos dois primeiros.

"""


vet1 = [1, 2, 3, 1, 4, 3, 1, 7, -3, 4]
vet2 = [4, 5, 6, 4, 5, 6, 2, 5, 5, 2]

def soma(vet1, vet2):
    novo_vet = []
    for i in range(len(vet1)):
        n = vet1[i] + vet2[i]
        novo_vet.append(n)

    return novo_vet

print(soma(vet1, vet2))
