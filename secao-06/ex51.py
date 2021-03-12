"""
51. Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de
1.5%. A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça programa que determine
o salário atual do funcionário.

"""

salario = 2000
aumento = 0.015
SalarioAtual = salario + (salario * aumento)
ano = 1996
Ano_Atual = int(input('Informe o ano Atual: '))
while ano <= Ano_Atual:
    ano += 1
    aumento *= 2
    SalarioAtual = SalarioAtual + (SalarioAtual * aumento)

print(f'Ano atual {Ano_Atual}: Aumento deste ano é {aumento}%: Salario atual é {"%.2f" % SalarioAtual}R$')
