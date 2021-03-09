"""
48. Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos
valores não ultrapassem quatro milhões.
    
"""

n = int(input('Digite um numero: '))
while n < 0:
    n = int(input('Digite um numero: '))

f = 0
f1 = 0
f2 = 1
soma = 0
par = []
while f <= n:
    f = f1 + f2
    f2 = f1
    f1 = f
    print(f, end=' ')
    if f % 2 == 0:
        soma += f
        par.append(f)
    if soma > 4000 * 1000:
        print('Valor ultrapassou o limite.')

print('\nOs valores Pares são: ' ,par)
print(f'O resultado da soma de todos os valores pares da sequência de Fibonacci é {soma}')
