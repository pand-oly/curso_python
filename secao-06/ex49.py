"""
49. O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do
seu salário. Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente
nela, pois está rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está 
rendendo 5% ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para
que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores
para as taxas.

"""

cont = 0
Valor_Atual_Carlos = int(input('Informe valor do salário de Carlos: '))
Valor_Atual_Joao = Valor_Atual_Carlos * 1/3

PercentualPoupanca = int(input('Informe o valor do percentual de rendimeto da cardeneta poupança: '))
poupanca = PercentualPoupanca / 100
PercentualRenda = int(input('Informe o valor do percentual de rendimeto da renda fixa: '))
renda = PercentualRenda / 100

Salario_inicial_Carlos = Valor_Atual_Carlos
Salario_inicial_Joao = Valor_Atual_Joao

while Valor_Atual_Joao < Valor_Atual_Carlos:
    Valor_Atual_Carlos += (Valor_Atual_Carlos * poupanca)
    Valor_Atual_Joao += (Valor_Atual_Joao * renda)
    cont += 1


print(f'{cont} meses para salário de João igaular ao de Carlos.\n')
             #Em detalhes para mostrar que toda conta esta certa
print(f'''salário de Calos é {"%.2f" % Salario_inicial_Carlos}R$ + {poupanca}% ao mês X {cont} Meses = valor 
        pertencente atual é {"%.2f" % Valor_Atual_Carlos}  R$\n''')

print(f'''salário de Calos  {"%.2f" % Salario_inicial_Joao}R$ + {renda}% ao mês X {cont} Meses = valor 
        pertencente atual {"%.2f" % Valor_Atual_Joao} R$''')
