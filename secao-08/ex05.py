"""
5. Faça uma função e um programa de teste para o cálculo do volume de uma esfera. Sendo que o
raio é passado por parâmetro. V = 4 / 3 * þ * R³

"""

def volume(r):
    v = 4 / 3 * 3.14 * (r ** 3)
    return v

print(volume(2))