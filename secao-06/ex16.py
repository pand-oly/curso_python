"""
16. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
números impares de 1 até N em ordem decrescente.

"""

n = int(input('Digite numero inteiro positivo: '))

while n < 0 or n % 2 != 0:
    n = int(input('Digite numero inteiro positivo: '))


for i in range(n, -1, -1):
    if i % 2 != 0:
        print(i)
