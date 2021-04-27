"""
69. Faça um programa que faça operações simples de frações:

• Crie e leia duas frações P e Q, compostas por numerador e denominador.
• Encontre o máximo divisor comum entre o numerador e o denominador, e simplifique as frações.
• Apresente a soma, a subtração, o produto e o quociente entre as frações lidas. 

Obs.: Cria uma função para cada item.

"""

def entrada():
    p = int(input('Digite um número: '))
    q = int(input('Digite outro número: '))
    return p, q

p, q = entrada()
print()

def tabuada():
    table = []
    for n in range(1, 21):
        table.append([])
        for i in range(1, 101):
            m = n * i
            table[n-1].append(m)
    
    return table

table = tabuada()

def mmc(numerador, denominador):     
    for l in range(0, 20):
        if numerador in table[l] and denominador in table[l]:
            divisor = l + 1
    
    n = p // divisor
    d = q // divisor
    print(f'mmc {divisor}, frações {n}/{d}')
    return n, d

n, d = mmc(p, q)

def soma(n, d):
    print('Soma = ', n + d)

def subtracao(n, d):
    print('subtração = ', n - d)

def multiplicacao(n, d):
    print('Produto = ', n * d)

def divisao(n, d):
    print('Quociente', n / d)

soma(n, d)
subtracao(n, d)
multiplicacao(n, d)
divisao(n, d)
