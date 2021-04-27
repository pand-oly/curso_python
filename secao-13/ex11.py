"""
11. Faça um programa no qual o usuário informa o nome do arquivo e uma palavra, e retorne
o número de vezes que aquela palavra aparece no arquivo.

"""

arquivo = input('Digite nome do arquivo: ')
palavra = input('Digite nome da palavras: ')

with open(arquivo, 'r') as fil:
    cont = len(fil.readlines())
    fil.seek(0)
    lista = list()
    for i in range(cont):
        variavel = fil.readline().split(' ')
        for p in variavel:
            lista.append(p)
    if palavra in lista:
        print(lista.count(palavra))
    else:
        print(0)
