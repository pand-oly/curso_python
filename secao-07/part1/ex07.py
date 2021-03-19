"""
7. Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima
o vetor, o maior elemento e a posição que ele se encontra.

"""

vetor = []
for i in range(0, 10):
    i = int(input('Informe um valor: '))
    vetor.append(i)

print('Vetor ' ,vetor)
print('Maior ', max(vetor))
print('Localização', vetor.index(max(vetor)))
