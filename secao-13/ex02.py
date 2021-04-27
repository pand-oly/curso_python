"""
2. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
linhas esse arquivo possui.


"""

fil = input('Digite nome do aquivo: ')

with open(fil, 'r') as fil:
    print(len(fil.readlines()))
