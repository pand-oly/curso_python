"""
15. Faça um programa que receba como entrada o ano corrente e o nome de dois arquivos:
um de entrada e outro de saída. Cada linha do arquivo de entrada contém o nome de uma pessoa
(ocupando 40 caracteres) e o seu ano de nascimento. O programa deverá ler o arquivo de entrada
e gerar um arquivo de saída onde aparece o nome da pessoa seguida por uma string que representa
a sua idade.

• Se a idade for menor do que 18 anos, escreva "menor de idade"
• Se a idade for maior do que 18 anos, escreva "maior de idade"
• Se a idade for igual a 18 anos, escreva "entrando na maior idade"

"""

from datetime import date

entrada = input('Digite nome do arquivo: ')
saida = input('Digite nome do novo arquivo: ')

def arquivo(entrada, saida):
    with open(entrada, 'r') as arq:
        cont = len(arq.readlines())
        arq.seek(0)
        hoje = date.today()
        for i in range(cont):
            nome, dia_Nacimento, mes_Nacimento, ano_Nacimento = arq.readline().split(' ')
            idade = hoje.year - int(ano_Nacimento) -((hoje.month, hoje.day) < 
                                                    (int(mes_Nacimento), int(dia_Nacimento)))
            if idade < 18:
                strg = 'Menor de idade'
            elif idade > 18:
                strg = 'Maior de idade'
            elif idade == 18:
                strg = 'Entrando na maior idade'
            with open(saida, 'a') as new:
                new.write(f'{nome} {idade} "{strg}" \n')

arquivo(entrada, saida)
