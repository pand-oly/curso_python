"""
6. Faça um programa que leia 10 inteiros e imprima sua média. 

"""

vetor = []
soma = 0
for i in range(0, 10):
    numb = int(input('Digite um valor: '))
    vetor.append(numb)
    soma = soma + numb
    media = soma / 10
print(f'media: {media}')
