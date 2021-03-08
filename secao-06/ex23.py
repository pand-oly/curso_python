"""
23. Faca um algoritmo que leia um número positivo e imprima seus divisores.

"""

n = int(input('Informe o numero: ')) 
for i in range(1, 100):
    if n % i == 0:
        print(i, end=', ')
    