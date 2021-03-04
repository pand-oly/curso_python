"""
39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário
atual e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento 
proporcionalmente maior do que os funcionários com um salário maior, e conforme o tempo de serviço na empresa,
cada funcionário irá receber um bônus adicional de salário. Faça um programa que leia:

• o valor do salário atual do funcionário; 
• o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário 
final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.
___________________________________________________________________
|___Salário Atual___|_Reajuste(%)__|_Tempo de Serviço_|___Bônus___|
| Até 500,00        |    25%       | Abaixo de 1 ano  | Sem bônus |
| Até 1000,00       |    20%       | De 1 a 3 anos    | 100,00    |
| Até 1500,00       |    15%       | De 4 a 6 anos    | 200,00    |
| Até 2000,00       |    10%       | De 7 a 10 anos   | 300,00    |
| Acima de 2000,00  | Sem reajuste | Mais de 10 anos  | 500,00    |
-------------------------------------------------------------------

"""

salario = float(input('Informe o salario: '))
tempo = float(input('Informe o tempo de serviço: '))

if salario <= 500:
  salario = salario + (salario * 0.25)
elif salario <= 1000:
    salario = salario + (salario * 0.2)
elif salario <= 1500:
    salario  = salario + (salario * 0.15)
else:
    salario <= 2000
    salario = salario + (salario * 0.1)

if tempo >= 1 and tempo <= 3:
    salario = salario + 100
elif tempo >= 4 and tempo <= 6:
    salario = salario + 200
elif tempo >= 7 and tempo <= 10:
    salario = salario + 300
elif tempo > 10:
    salario = salario + 500

print(f'Novo Salario: R${salario}')