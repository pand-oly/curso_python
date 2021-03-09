"""
47. Faça um programa que apresente um menu de opções para o cálculo das seguintes
operações entre dois números:

• adição (opção 1)
• subtração (opção 2)
• multiplicação (opção 3)
• divisão (opção 4).
• saída (opção 5)

O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta 
ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5).

"""

opcoes = int(input('''Escolha uma das segintes opções:
                    \n• Adição (opção 1)
                    \n• Subtração (opção 2)
                    \n• Multiplicação (opção 3)
                    \n• Divisão (opção 4).
                    \n• Saída (opção 5)
 '''))
if opcoes < 1 or opcoes > 5:
    print('Opção invalida... escolha uma opção ou digite 5 para sair.\n')
    opcoes = int(input('''Escolha uma das segintes opções:
                    \n• Adição (opção 1)
                    \n• Subtração (opção 2)
                    \n• Multiplicação (opção 3)
                    \n• Divisão (opção 4).
                    \n• Saída (opção 5)
 '''))

while opcoes < 1 or opcoes > 5 or opcoes != 5:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número '))
    if opcoes == 1:
        a = num1 + num2
        print(f'Adção: {num1} + {num2} = {a} ')
    elif opcoes == 2:
        s = num1 - num2
        print(f'Subtração: {num1} - {num2} = {s} ')
    elif opcoes == 3:
        m = num1 * num2
        print(f'Multiplicação: {num1} * {num2} = {m} ')
    elif opcoes == 4:
        d = num1 // num2
        print(f'Divisão: {num1} / {num2} = {d} ')

    opcoes = int(input('''Escolha uma das segintes opções:
                    \n• Adição (opção 1)
                    \n• Subtração (opção 2)
                    \n• Multiplicação (opção 3)
                    \n• Divisão (opção 4).
                    \n• Saída (opção 5)\n'''))

print('Sair')