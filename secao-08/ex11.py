"""
11. Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra
for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular
a média ponderada, com pesos 5, 3 e 2

"""

def media(num1, num2, num3, var):
    if var.upper() == 'A':
        return (num1 + num2 + num3) / 3
    elif var.upper() == 'P':
        return (num1 + num2 + num3) / 10
    
    return "Letra incorreta"

num1 = int(input('Informe primeira nota: '))
num2 = int(input('Informe segunda nota: '))
num3 = int(input('Informe terceira nota: '))
var = input('Digite "A" para media arintimética e "P" para media ponderada: ')

print(media(num1, num2, num3, var))
