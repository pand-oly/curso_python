"""
37. Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... > A11, ou seja,
está ordenado em ordem crescente até o sexto elemento, e a partir desse elemento está ordenado
em ordem decrescente. Dado o vetor da questão anterior, proponha um algoritmo para ordenar os
elementos.

"""

vetor = list(range(1, 12))
print(vetor)

a = []
for i in range(0, 6):
    a.append(vetor[i])

inverso = []
for i in range(6, 11):
    inverso.append(vetor[i])

final = a + inverso[::-1]
print(final)