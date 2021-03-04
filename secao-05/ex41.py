"""
41. Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo
com a tabela abaixo:
__________________________________________________
|________IMC_______|________Classificação________|
| <18,5            | Abaixo do Peso              |
| 18,6 - 24,9      | Saudável                    |
| 25,0 - 29,9      | Peso em excesso             |
| 30,0 - 34,9      | Obesidade Grau 1            |
| 35,0 - 39,9      | Obesidade Grau 2(severa)    |
| > 40,0           | Obesidade Grau Ill(mórbida) |
--------------------------------------------------

"""

imc = float(input('Informe seu IMC: '))

if imc <= 18.5:
    print('Abaixo do Peso')
elif imc >= 18.6 and imc <= 24.9:
    print('Saudável')
elif imc >= 25 and imc <= 29.9:
    print('Peso em excesso')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Grau 1')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade Grau 2(severa)')
else:
    imc >= 40
    print('Obesidade Grau Ill(mórbida)')