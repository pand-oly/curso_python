"""
3. Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o numero ao quadrado.

"""

num = float(input('Informe um número: '))

if num >= 0:
    print(num ** 0.5)
else:
    print(num ** 2)
