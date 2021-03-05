"""
12. Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem decrescente.

"""
n = int(input('Digite numero inteiro positivo: '))

while n < 0 or n % 2 != 0:
    n = int(input('Digite numero inteiro positivo: '))

if n >= 0 and n % 2 == 0:
    for i in range (n, -1, -1):
        print(i)
else:
    ()