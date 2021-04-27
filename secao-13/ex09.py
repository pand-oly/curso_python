"""
9. Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com
o conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo).

"""

fil01 = input('Digite nome do arquivo: ')
fil02 = input('Digite nome do outro arquivo: ')

with open('new_file.txt', 'a') as new:
    with open(fil01, 'r') as fil:
        for i in fil:
            new.write(i)
    
    with open(fil02, 'r') as fil:
        for i in fil:
            new.write(i)
        