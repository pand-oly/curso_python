"""
9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso
contrário imprima:Empréstimo concedido.

"""

salario = float(input('Infome seu salário: '))
prestacao = float(input('Informe o valor da prestação do empréstimo: '))

percentual = salario * 0.2

if prestacao > percentual:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
