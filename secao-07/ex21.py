"""
21. Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada.
Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C.

"""

VetorA = []
VetorB = []
VetorC = []
c = 0
print('Digite 10 números para o vetor A.')
for a in range(0, 10):
    c += 1
    num = int(input(f'{c}/10 Digite um númeor intero para A: '))
    VetorA.append(num)

c = 0
print('Digite 10 números para o vetor B.')
for b in range(0, 10):
    c += 1
    num = int(input(f'{c}/10 Digite um númeor intero para B: '))
    VetorB.append(num)

for c in range(0, 10):
    calculo = VetorA[c] - VetorB[c]
    VetorC.append(calculo)

print('Vetor A', VetorA)
print('Vetor B', VetorB)
print('Vetor C', VetorC)
