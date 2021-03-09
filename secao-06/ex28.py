"""
28. Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E,
conforme a fórmula a seguir

E= 1 + 1 / 1! + 1 / 2! + 1/3! + ... + 1/N!

"""

e = 1
n = int(input('Informe um número: '))
for i in range(1, n + 1):
    e = (1/i) + e

print(f'E = {e}')