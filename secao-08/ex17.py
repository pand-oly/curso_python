"""
17. Faça uma função que receba dois números inteiros positivos por parâmetro e retorne a soma
dos N números inteiros existentes entre eles.

"""

def parametro(n1, n2):
    soma = 0
    for n in range(n1 + 1, n2):
        soma += n
    return soma

print(parametro(1, 5))
