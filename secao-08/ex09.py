"""
9. Faça umam função que receba a altura e o raio de um cilindro circular e retorne o volume
do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula:
V = þ * raio² * altura, onde þ = 3.141592.

"""

def volume(h, r):
    v = 3.141592 * (r ** 2) * h
    return v

h = int(input('Infome valor da altura: '))
r = int(input('Informe valor do volume: '))

print(volume(h, r))
