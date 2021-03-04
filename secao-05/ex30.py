"""
30. Faça um programa que receba três números e mostre-os em ordem crescente.

"""

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))

if num1 < num2 and num1 < num3:
    if num2 < num3:
        print(f'{num1}, {num2}, {num3}')
    else:
        print(f'{num1}, {num3}, {num2}')
elif num2 < num3 and num2 < num1:
    if num1 < num3:
        print(f'{num2}, {num1}, {num3}')
    else:
        print(f'{num2}, {num3}, {num1}')
elif num3 < num2 and num3 < num1:
    if num2 < num1:
        print(f'{num3}, {num2}, {num1}')
    else:
        print(f'{num3}, {num1}, {num2}')
