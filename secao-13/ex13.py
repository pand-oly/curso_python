"""
13. Faça um programa que permita que o usuário entre com diversos nomes e telefone para cadastro,
e crie um arquivo com essas informações, uma por linha. O usuário finaliza a entrada com 'O' para
o telefone.

"""

def cadastro():
    telefone = 'O'
    while telefone != '0':
        nome = input('Digeite nome para cadastro: ')
        telefone = input('Digite número de telefone: ')
        with open('cadastro.txt', 'a') as arq:
            arq.write(nome + ' ' + telefone + ' \n')

cadastro()
