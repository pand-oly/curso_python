"""
26. Leia a distância em 'Km' e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em 'Km/l' e escreva uma mensagem de acordo com a tabela abaixo:

CONSUMO   | (Km/l)   |      MENSAGEM
menor que |   8      |   Venda o carro!
entre     | 8 e 14   |       Econômico!
maior que |  12      | Super econômico!
 
"""

d = int(input('Informe a distancia percorrida: '))
l = int(input('Informe a quantidade de litros consumidos: '))

c = d / l

if c < 8:
    print('Venda o carro!')
elif c >= 8 and c <= 14:
    print('Econômico!')
    if c > 12:
        print('Super econômico!')
