"""
10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, 
utilizando as seguintes fórmulas (onde h corresponde à altura) 
• Homens: (72.7 * h) - 58
• Mulheres (62.1 * h) - 44.7

"""

sexo = input('Informe seu gênero (M / F): ')
h = float(input('Informe sua altura: '))

if sexo.upper() == 'M':
    PesoIdeal = (72.7 * h) - 58
    print(f'O seu peso ideal é: {"%.2f" % PesoIdeal}')
if sexo.upper() == 'F':
    PesoIdeal = (62.1 * h) - 44.7
    print(f'O seu peso ideal é: {"%.2f" % PesoIdeal}')
