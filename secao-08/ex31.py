"""
31. Faça uma função para calcular o número neperiano usando uma série. A função deve ter como
parâmetro o número de termos que serão somados (note que, quanto maior o número, mais próxima
a resposta estará do valor e).
! formula

"""

def serie(n):
    e = 0
    for i in range(n):
        f = 1
        for n in range(i, 0, -1):
            f *= n
        e += 1 / f
    return e

n = int(input('Digite um número: '))
print(serie(n))
