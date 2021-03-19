"""
30. Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção
entre os 2 vetores anteriores, ou seja, que contém apenas os números que estão em ambos os
vetores. Não deve conter números repetidos.

"""

vetor1 = set({})
vetor2 =  set({})
for v in range(0, 10):
    num = int(input('Informe um número: '))
    vetor1.add(num)

for v in range(0, 10):
    num = int(input('Informe um número: '))
    vetor2.add(num)

for i in vetor1:
    if i in vetor2:
        vetorI = vetor1.intersection(vetor2)  #Ou pose usar 0 & para fazer mesma função

print(vetorI)