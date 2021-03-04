"""
6. Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles, 
assim como a diferença entre eles

"""

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if num1 > num2:
    print(f'O número {num1} é maior, a diferença entre eles é {num1 - num2}')
else:
    print(f'O número {num2} é maior, a diferença entre eles é {num2 - num1}')
