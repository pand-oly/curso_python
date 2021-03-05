"""
9. Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

"""

n = int(input('Informe um número inteiro: '))
 
contador, aux = 1, 1
 
while contador <= n:
    if aux % 2 != 0:
        print(aux)
        contador = contador + 1
    aux = aux + 1
