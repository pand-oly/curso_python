"""
40. Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo.
O programa tem que retornar o maior e o menor número lido. 

"""

menor = 999
maior = 0
n = int(input('Informe um numero: '))
while n >= 0:
    n = int(input('Informe um numero: '))
    if n > maior and n >= 0:
        maior = n
    if n < menor and n >= 0:
        menor = n

print(maior)
print(menor)