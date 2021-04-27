"""
33. Faça uma função que receba um número N e retorne a soma dos algarismos de N!. Ex:
se N = 4, N! = 24. Logo, a soma de seus algarismos é 2 + 4 = 6.

"""

def fatorial(n):
    f = 1
    for n in range(n, 0, -1):
        f *= n
    
    return f


def algarismo(f):
    f = str(f)
    soma = 0
    for n in f:
        n = int(n)
        soma += n
    
    return soma 

n = int(input('Digite um número: '))
numero = fatorial(n)
print(algarismo(numero))
