"""
33. Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições
com valor zero. Para isso, todos os elementos à frente do valor zero, devem ser movidos uma
posição para trás no vetor.

"""

vetor = [0, 6, 4, 0, 8, 10, 11, 15, 0, 12, 3, 2, 0]
cont = vetor.count(0)
while cont > 0:
    vetor.pop(vetor.index(0))
    cont = vetor.count(0)

print(vetor)


#Metodo que vi nas respostas do professor

vetor = [valor for valor in vetor if valor > 0]

print(vetor)