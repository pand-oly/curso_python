"""
55. Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números primos.

"""

n = int(input('Informe um número: '))
s = 0
for i in range(1, n):
    if i == 2:
        s += i
    if i == 3:
        s += i
    if i == 5:
        s += i
    if i == 7:
        s += i
    if i == 11:
        s += i
    if i == 13:
        s += i
    
print(s)
