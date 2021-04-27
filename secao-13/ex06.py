"""
6. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
vezes cada letra do alfabeto aparece dentro do arquivo.

"""

alfabeto = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
            'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

fil = input('Digite nome do arquivo: ')

with open(fil, 'r') as fil:
    for i in fil.read():
        if i.lower() in alfabeto:
            alfabeto[i.lower()] += 1

print(alfabeto)
