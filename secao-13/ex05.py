"""
5. Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre na tela
quantas vezes aquele caractere ocorre dentro do arquivo.

"""

fil = input('Digite nome do aquivo: ')
letra = input('Digite uma letra: ')
with open(fil, 'r') as fil:
    cont = 0
    for i in fil.read():
        if i.lower() == letra.lower():
            cont += 1

print(cont)
