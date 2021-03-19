"""
38. Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores,
guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao final na tela os
valores em ordem.

"""

vetor = []
for v in range(0, 10):
    num = int(input('Digite um número para o vetor: '))
    vetor.append(num)

vetor.sort()
print(vetor)
