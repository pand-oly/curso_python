"""
56. Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões.

"""

n = 2_000_000
soma = 0
for i in range(2, n + 1):
    if i == 2 or i == 3 or i == 5 or i == 7 or i == 11:
        soma += i
    elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and  i % 11 != 0:
        soma += i

print(soma)