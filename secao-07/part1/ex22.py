"""
22. Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo,
nas posições pares os valores do primeiro e nas posições impares os valores do segundo.

"""
vetor1 = []
vetor2 = []
vetor3 = []
c = 0
print('Digite 10 números para o primeiro vetor.')
for a in range(0, 10):
    c += 1
    num = int(input(f'{c}/10 Digite um númeor intero para o primeior vetor: '))
    vetor1.append(num)

c = 0
print('Digite 10 números para o segundo vetor.')
for b in range(0, 10):
    c += 1
    num = int(input(f'{c}/10 Digite um númeor intero para o segundo vetor: '))
    vetor2.append(num)

cont1 = 0
cont2 = 0
for i in range(0, 20):
    if i % 2 == 0:
        vetor3.append(vetor1[cont1])
        cont1 += 1
    else:
        vetor3.append(vetor2[cont2])
        cont2 += 1

print(vetor1)
print(vetor2)
print(vetor3)
