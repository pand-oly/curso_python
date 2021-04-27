"""
2. Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela
no formato textual por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de 2000.

"""

def data(dia, mes, ano):
    if mes == 1:
        return f'{dia} de Janeiro de {ano}'
    elif mes == 2:
        return f'{dia} de Fevereiro de {ano}'
    elif mes == 3:
        return f'{dia} de Março de {ano}'
    elif mes == 4:
        return f'{dia} de Abril de {ano}'
    elif mes == 5:
        return f'{dia} de Maio de {ano}'
    elif mes == 6:
        return f'{dia} de Junho de {ano}'
    elif mes == 7:
        return f'{dia} de Julho de {ano}'
    elif mes == 8:
        return f'{dia} de Agosto de {ano}'
    elif mes == 9:
        return f'{dia} de Setembro de {ano}'
    elif mes == 10:
        return f'{dia} de Outubro de {ano}'
    elif mes == 11:
        return f'{dia} de Novembro de {ano}'
    elif mes == 12:
        return f'{dia} de Dezembro de {ano}'
    return 0


varData = input('Informe a data: ')

dia, mes, ano = varData.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)

print(data(dia, mes, ano))