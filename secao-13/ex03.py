"""
3. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
letras são vogais.

"""

fil = input('Digite nome do aquivo: ')
vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

with open(fil, 'r') as fil:
    cont = 0
    for i in fil.read():
        if i in vogais:
            cont += 1

#Não vou colocar as letras com acentos por que não preciso gastar este tempo com um exercicio
    print(cont)
