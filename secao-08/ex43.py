"""
43. Faça uma função que receba um vetor de inteiros e o preencha com números aleatórios
sem repetição.

"""

from random import *

vetor = set()

def v(vetor):
    for i in range(0, 10):
        n = randint(0, 99)
        vetor.add(n)
    
    return vetor

print(v(vetor))