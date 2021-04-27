"""
26. Faça um algoritmo que receba um número inteiro positivo n e calcule o somatório de 1 até n.

"""

def somatorio(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma

n = int(input("Digite um número: "))
print(somatorio(n))
