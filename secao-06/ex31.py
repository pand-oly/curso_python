"""
31. Faça um programa que calcule e escreva o valor de S

S = 1 + 3 + 5 + 7 ..... 99
    1   2   3   4       50

"""
f = 0
s = 0
d = 0
n = int(input('Informe o valor desejado: '))
for i in range(1, n + 1):
    if i % 2 != 0:
        d = d + 1
        f = i / d
        s = s + f

print(f'O valor de S = {s}')