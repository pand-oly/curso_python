"""
13. Faça uma função que receba dois valores numéricos e um símbolo. Este símbolo repre sentará a
operação que se deseja efetuar com os números. Se o símbolo for + deverá ser realizada uma adição,
se for – uma subtração, se for / uma divisão e se for * será efetuada uma multiplicação.

"""

def operacao(s, num1, num2):
    if s == '+':
        return num1 + num2
    elif s == '-':
        return num1 - num2
    elif s == '/':
        return num1 // num2
    elif s == '*':
        return num1 * num2
    return 'Símbolo invalido'

num1 = int(input('Informe um número: '))
s = input('Informe símbolo da operação desejada: ')
num2 = int(input('Informe outro número: '))

print(operacao(s, num1, num2))
