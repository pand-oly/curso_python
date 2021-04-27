"""
20. Faça um algoritmo que receba um número inteiro positivo n e calcule o seu fatorial, n!.

"""
def fatorial(numero):
    f = 1
    for n in range(numero, 0, -1):
        f *= n
    
    return f

numero = int(input('Informe um número: '))
print(fatorial(numero))
