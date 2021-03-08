"""
25. Faça um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 ou 5.

"""

multiplo3 = 0
multiplo5 = 0
soma = 0
for i in range(0, 1000):
    if i % 3 == 0:
        multiplo3 = i
        soma = soma + multiplo3
    if i % 5 == 0:
        multiplo5 = i
        soma = soma + multiplo5

print(soma)
