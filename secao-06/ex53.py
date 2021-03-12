"""
53. Escreva um programa que leia um número inteiro positivo N e em seguida imprima N linhas do chamado 
Triângulo de Floyd. Para n = 6, temos:

1
2 3
4 5 6 
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21

"""
n = int(input('Informe o valor de n para Triângulo de Floyd: '))
if n > 0:
    for i in range(1, 7):
        for c in range(1, i + 1):
            print(f'{n:<3}', end=" ")
            n += 1
        print('')
else: 
    print('Valor invalido = ou < a 0')

