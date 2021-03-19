"""
8. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
na ordem inversa.

"""

vetor = []
for i in range(0, 6):
    num = int(input('Informe um valor: '))
    vetor.append(num)

print(vetor[::-1])