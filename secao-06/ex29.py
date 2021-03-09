"""
29. Escreva um programa para calcular o valor da série, para 5 termos.

S= 0 + 1/2!+ 2/4! + 3/6! + ...

"""

s = 0
n = int(input('Informe um número: '))
for i in range(1, n + 1):
    s = (1/i) + s

print(f'S = {s}')