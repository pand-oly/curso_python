"""
14. Dado um arquivo contendo um conjunto de nome e data de nascimento (DD MM AAAA, isto é, 3
inteiros em sequência), faça um programa que leia o nome do arquivo e a data de hoje e construa
outro arquivo contendo o nome e a idade de cada pessoa do primeiro arquivo.

"""

from datetime import date

arquivo = input('Digite nome do arquivo: ')

def idade(arq):
    with open(arq, 'r') as arq:
        cont = len(arq.readlines())
        arq.seek(0)
        hoje = date.today()
        for i in range(cont):
            nome, dia_Nacimento, mes_Nacimento, ano_Nacimento = arq.readline().split(' ')
            idade = hoje.year - int(ano_Nacimento) -((hoje.month, hoje.day) < 
                                                    (int(mes_Nacimento), int(dia_Nacimento)))
            with open('new-file-ex14.txt', 'a') as new:
                new.write(f'{nome} {idade} \n')

idade(arquivo)
