"""
44. Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número
superior ao número lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 
0 1 1 2 3 5 8 13 21 34.

"""
n = int(input('Digite um numero: '))
while n < 0:
    n = int(input('Digite um numero: '))

f = 0
f1 = 0
f2 = 1

while f <= n:
    print(f, end=' ')
    f = f1 + f2
    f2 = f1
    f1 = f

print(f)
