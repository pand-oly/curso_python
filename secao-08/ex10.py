"""
10. Faça uma função que receba dois números e retorne qual deles é o maior.

"""

def maior(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    return 'Iguais'

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

print(maior(num1, num2))
