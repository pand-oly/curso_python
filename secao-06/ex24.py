"""
24. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, 
com exceção dele próprio. Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

"""

n = int(input('Informe o numero: '))
soma = 0
for i in range(1, 100):
    if n % i == 0:
        if n != i:
            soma = i + soma

print(soma)