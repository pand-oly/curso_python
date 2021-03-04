"""
7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem Números iguais.

"""

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if num1 > num2:
    print(f'O número {num1} é maior')
elif num1 < num2:
    print(f'O número {num2} é maior')
else:
    print('Números iguais')
