"""
14. Faça uma função que receba a distância em Km e a quantidade de litros de gasolina consumidos
por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a
tabela abaixo:
________________________________________
|CONSUMO   | (Km/l) |    MENSAGEM       |
|menor que |   8    |  Venda o carro!   |
|entre     | 8 e 14 |  Econômico!       |
|maior que |   12   |  Super econômico! |
-----------------------------------------

"""

def pesquisa(km, l):
    c = km / l
    if c < 8:
        return 'Venda o carro!'
    elif c >= 8 and c <= 14:
        return 'Econômico!'
    elif c > 12:
        return 'Super econômico!'

km = int(input('Informe a distancia percorrida: '))
l = int(input('Informe a quantidade de litros consumidos: '))

print(pesquisa(km, l))
