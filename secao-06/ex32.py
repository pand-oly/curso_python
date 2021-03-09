"""
32. Faça um programa que simula o lançamento de dois dados, d1 e d2, N vezes, e tem como saída o número de
cada dado e a relação entre eles >,<,=) de cada lançamento. 

"""

q = int(input('Quantas vezes fazer a pergunta: '))
for i in range(1, q + 1):
    d1 = int(input('Digite um número: '))
    d2 = int(input('Digite um número: '))
    if d1 > d2:
        print('D1 é maior')
    elif d2 > d1:
        print('D2 é maior')
    else:
        print('Iguais')