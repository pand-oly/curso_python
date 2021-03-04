"""
31. Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostra qual a classificação dessa pessoa.


| Altura         |               Peso
|                |
|                | Até 60  |   Entre 60 e 90 (Inclusive)  | Acima de 90 |
|Menor que 1,20  |   A     |            D                 |      G      |
|De 1,20 a 1,70  |   B     |            E                 |      H      |
|Maior que 1,70  |   C     |            F                 |      I      |

"""

altura = float(input('Informe o sua altura: '))
peso = float(input('Informe seu peso: '))

if altura < 1.2:
    if peso < 60:
        print('Grupo A')
    elif peso >= 60 and peso <= 90:
        print('Grupo D')
    elif peso > 90:
        print('Grupo G')
elif altura >= 1.2 and altura < 1.70:
    if peso < 60:
        print('Grupo B')
    elif peso >= 60 or peso <= 90:
        print('Grupo E')
    elif peso > 90:
        print('Grupo H')
elif altura >= 1.7:
    if peso < 60:
        print('Grupo C')
    elif peso >= 60 and peso <= 90:
        print('Grupo F')
    elif peso > 90:
        print('Grupo I')