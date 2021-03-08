"""
17. Faça um programa que leia um número inteiro positivo ne calcule a soma dos n primeiros
números naturais.

"""
n = int(input('Informe um número inteiro: '))

contador, aux = 1, 1
soma = 0

while contador <= n:
    if aux % 2 == 0:
        soma = aux + soma
        contador = contador + 1
    aux = aux + 1

print(soma)