"""
28. Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:

(a) Geométrica:  ³√x * y * z 

(b) Ponderada: x + 2 * y + 3 * z 
|                      6      

(c) Harmônica:      1
|               1 + 1 + 1
|               x   y   z

(d) Aritmética: x + y + z
|                   3

"""

x = int(input('Informe o numero de x: '))
y = int(input('Informe o numero de y: '))
z = int(input('Informe o numero de z: '))
operacao = input('''Informe sua escolha:
(a) Geométrica
(b) Ponderada
(c) Harmônica            
(d) Aritmética
''')

if operacao.lower() == 'a':
    m = x * y * z
    g = m ** (1/3)
    print(f'Escolha Geométrica: ³√ {x} * {y} * {z}')
    print(f'Resultado é: {g}')
elif operacao.lower() == 'b':
    m = x + 2 * y + 3 * z
    p = m / 6
    print(f'Escolha média Ponderada:\nResultado é = {p}')
elif operacao.lower() == 'c':
    s = (1 / x) + (1 / y) + (1 / z)
    h = 3 / s
    print(f'Escolha média Harmônica:\nResultado é = {h}')
elif operacao.lower() == 'd':
    a = (x + y + z) / 3
    print(f'Escolha média Aritmédica:\nResultado é = {a}')
