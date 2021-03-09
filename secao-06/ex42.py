"""
42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um
dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou
zero.

"""
n = int(input('DIgite um número: '))
while n > 0:
    q = n ** 2
    print(q)
    c = n ** 3
    print(c)
    r = n ** 0.5
    print(r)
    n = int(input('DIgite um número: '))
