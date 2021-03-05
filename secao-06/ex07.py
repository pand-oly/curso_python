"""
7. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

"""

vetor = []
soma = 0
m = 0
for i in range(0, 10):
    numb = int(input('Digite um valor: '))
    vetor.append(numb)
    if numb % 2 == 0:
        m = m + 1
        soma = soma + numb
        media = soma / m
print(f'media: {media}')