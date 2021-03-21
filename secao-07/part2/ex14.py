"""
14. Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo.
Sabendo que cada cartela deverá conter 5 linhas de 5 números, gere estes dados de modo a não
ter números repetidos dentro das cartelas. O programa deve exibir na tela a cartela gerada.

#!uau
"""

import random
vet = []
vetB = []
vetAux = []
num = 0
conta = 0
for i in range(25):
    num = random.randint(0, 99)
    while num in vet:
        num = random.randint(0, 99)
    vet.append(num)
print()
for i in range(5):
    vetAux.clear()
    for x in range(5):
        vetAux.append(vet[conta])
        conta += 1
    vetB.append(vetAux.copy())
for i in range(len(vetB)):
    for x in range(len(vetB)):
        print(f'[{vetB[i][x]:^2}]', end=' ')
    print('')