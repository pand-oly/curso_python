"""
25. Faça uma função que receba um inteiro N como parâmetro, calcule e retorne o resultado da
seguinte série:

S = 2/4 + 5/5 + 10/6 + ... + (N² + 1)/(N +3)

"""

def calculo(n):
    s = [(v ** 2 + 1) / (v + 3) for v in range(1, n + 1)]
    return round(sum(s), 2)

n = int(input('Digite um número: '))
print(calculo(n))
