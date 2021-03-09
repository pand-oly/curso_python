"""
39. Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário.
Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.

"""

h = int(input('Informe o valor da altura: '))
b = int(input('Informe o valor da base: '))
while h <= 0 or b <= 0:
    h = int(input('Informe o valor da altura: '))
    b = int(input('Informe o valor da base: '))

a = (h * b) / 2

print(a)