"""
10. Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de
entrada contém em cada linha o nome de uma cidade (ocupando 40 caracteres) e o seu número de
habitantes. O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece
o nome da cidade mais populosa seguida pelo seu número de habitantes.

"""

entrada = 'ex10-cidades.txt'
saida = 'ex10-saida.txt'

def mapa(entrada):
    list_Chaves = list()
    list_Valores = list()
        
    with open(entrada, 'r') as entrada:
        linhas = len(entrada.readlines())
        entrada.seek(0)
        for i in range(linhas):
            chave, valor = entrada.readline().split('- ')
            valor = int(valor)
            list_Chaves.append(chave)
            list_Valores.append(valor)
    
    return list_Chaves, list_Valores


def organize(saida, lista1, lista2):
    #print(saida, lista1, lista2)
    lista3 = list(reversed(sorted(lista2.copy())))
    with open(saida, 'a') as saida:
        for i in lista3:
            index = lista2.index(i)
            line = f'{lista1[index]} - {lista2[index]}'
            saida.write(f'{line}\n')


lista1, lista2 =  mapa(entrada)
organize(saida, lista1, lista2)
