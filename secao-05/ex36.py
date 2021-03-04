"""
36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. 
Para calcular a comissão, considere a tabela abaixo:
____________________________________________________________________________________
|__________Venda mensal________________________________|______Comissão ____________|
|Maior ou igual a R$100.000,00                         | R$700,00 + 16% das vendas |
|Menor que R$100.000,00 e maior ou igual a R$80.000,00 | R$ 650,00 +14% das vendas |
|Menor que R$80.000,00 e maior ou igual a R$60.000,00  | R$600,00 +14% das vendas  |
|Menor que R$60.000,00 e maior ou igual a R$40.000,00  | R$550,00 +14% das vendas  |
|Menor que R$40.000,00 e maior ou igual a R$20.000.00  | R$500.00 +14% das vendas  |
|Menor que R$20.000,00                                 | R$400,00 +14% das vendas  |
------------------------------------------------------------------------------------

"""

valor = float(input('Informe o valor da venda: '))

if valor >= 100_000:
    comissao = valor + (valor * 0.16) + 700
    print(f'Comissão do vendedor sera de R${"%.2f" % comissao}')
elif valor < 100_000 and valor >= 80_000:
    comissao = valor + (valor * 0.14) + 650
    print(f'Comissão do vendedor sera de R${"%.2f" % comissao}')
elif valor < 80_000 and valor >= 60_000:
    comissao = valor + (valor * 0.14) + 600
    print(f'Comissão do vendedor sera de R${"%.2f" % comissao}')
elif valor < 60_000 and valor >= 40_000:
    comissao = valor + (valor * 0.14) + 550
    print(f'Comissão do vendedor sera de R${"%.2f" % comissao}')
elif valor < 40_000 and valor >= 20_000:
    comissao = valor + (valor * 0.14) + 500
    print(f'Comissão do vendedor sera de R${"%.2f" % comissao}')
elif valor < 20_000:
    comissao = valor + (valor * 0.14) + 400
    print(f'Comissão do vendedor sera de R${"%.2f" % comissao}')