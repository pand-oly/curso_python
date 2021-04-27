"""
16. Faça um programa que recebe um vetor de 10 números, converta cada um desses números para
binário e grave a sequência de Os e 1s em um arquivo texto. Cada número deve ser gravado em 
uma linha.

"""

numeros = [1, 2, 3, 4, 5, 6, 7, 80, 9, 20]
with open('ex16-arquivo.txt', 'a') as arquivo:
    for n in numeros:
        arquivo.write(f'{n:08b} \n')

