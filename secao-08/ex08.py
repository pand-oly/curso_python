"""
8. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = Raiz²{(a2 + b2) * 1/2}. Faça uma função que receba os valores de a e b e calcule o
valor da hipotenusa através da equação.

"""

def hipotenusa(a, b):
    h = (a ** 2 + b ** 2) ** (1/2)
    return h

a = int(input('Informe valor de A: '))
b = int(input('Informe valor de B: '))

print(hipotenusa(a, b))
