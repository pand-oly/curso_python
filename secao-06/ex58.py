"""
58. Faça um programa que some os números primos existentes entre a e b, onde a e b são
números informados pelo usuário.

"""

print('A e B devem ser maiores que 1')
a = 0
b = 0
while a <= 1:
    a = int(input('Informe valor de A: '))
while b <= 1:
    b = int(input('Informe valor de B: '))
soma = 0

for i in range(a, b + 1):
    if i == 2 or i == 3 or i == 5 or i == 7 or i == 11:
        soma += i
    elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and  i % 11 != 0:
        soma += i

print(f'Soma dos numeros dentre A e B é = {soma}')