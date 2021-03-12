"""
59. Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kw/h, e 
para cada habitante entre com os seguintes dados: consumo do mês e o código do consumidor (1-Residencial,
2-Comercial, 3-Industrial). No final imprima o maior, o menor e a média do consumo dos habitantes; e por 
fim o total do consumo de cada categoria de consumidor.

"""

habit = int(input('Informe N° de moradores: '))
print('Atenção aos codigos:\n1-Residencial,\n2-Comercial,\n3-Industrial')
maior = 0
menor = 9999999
h = 0
s = 0
while h < habit:
    h += 1
    cod = int(input('\nInforme o codigo do consumidor: '))
    if cod == 1:
        inf = '1-Residencial'
    elif cod == 2:
        inf = '2-Comercial'
    elif cod == 3:
        inf = '3-Industrial'
    else:
        print('Codigo do consumidor errado informe o codigo corretamente')
        cod = int(input('\nInforme o codigo do consumidor: '))

    cons = int(input('Informe o consumo do mês: '))

    if cons > maior:
        maior = cons
        mai = h
    if cons < menor:
        menor = cons
        men = h
    s += cons
    print(f'\nO habitante {h} cod: {inf}, consumiu {cons} kwh')

media = s / habit
print(f'\nA media do consumo total foi: {media} kwh')
print(f'\nO maior consumidor foi {mai} consumo {maior} kwh')
print(f'\nO menor consumidor foi {men} consumo {menor} kwh')
