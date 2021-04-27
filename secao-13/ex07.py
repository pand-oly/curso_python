"""
7. Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto
contendo o texto do arquivo de entrada, mas com as vogais substituídas por '*'.

"""

vogais = ['a','e', 'i', 'o', 'u']
fil = input('Digite nome do arquivo: ')

with open('new_file.txt', 'a') as nwf:
    with open(fil, 'r') as fil:
        for i in fil.read():
            if i.lower() in vogais:
                i = '*'
            nwf.write(i)
