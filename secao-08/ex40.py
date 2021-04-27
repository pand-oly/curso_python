"""
40. Faça uma função que receba um vetor de inteiros e retorne quantos valores pares ele possui.

"""

def v(vetor):
    return len(vetor)

n = ''
vetor = []
while n != 0:
    n = int(input('Digite um número: '))
    vetor.append(n)

print(v(vetor))
