"""
18. Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os
múltiplos de um número inteiro x num vetor e mostre-os na tela.

"""

vetor = []
for v in range(0, 10):
    num = int(input('Informe um número: '))
    vetor.append(num)

x = int(input('Informe valor de x: '))
multiplos = []
for i in vetor:
    if i % x == 0:
        multiplos.append(i)

print(f'Multiplos de {x} = {multiplos}')
