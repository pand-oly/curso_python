"""
18. Faça um programa que mostre ao usuário um menu com 4 opções de operações ma temáticas 
(as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois valores 
numéricos e realiza a operação, mostrando o resultado e saindo.

"""

operacoes = input('Informe a operação que deseja: " + ", " - ", " * ", " / "  ')

if operacoes == "+":
    numero1 = int(input('Informe um número: '))
    numero2 = int(input('Informe outro número: '))
    print(f'O resultado da soma é {numero1 + numero2}')
elif operacoes == "-":
    numero1 = int(input('Informe um número: '))
    numero2 = int(input('Informe outro número: '))
    print(f'O resultado da subtração é {numero1 - numero2}')
elif operacoes == "*":
    numero1 = int(input('Informe um número: '))
    numero2 = int(input('Informe outro número: '))
    print(f'O resultado da multiplicação é {numero1 * numero2}')
elif operacoes == "/":
    numero1 = int(input('Informe um número: '))
    numero2 = int(input('Informe outro número: '))
    print(f'O resultado da divisão é {numero1 / numero2}')
