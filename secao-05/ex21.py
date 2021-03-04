"""
21. Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. 
Escreva uma mensagem de erro se a opção for inválida.

Escolha a opção: 
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).
Opção 

"""

menu = int(input("""Escolha a opção: 
1- Soma de 2 números.
2- Diferença entre 2 números (maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).\n"""))

if menu == 1:
    numero1 = int(input('informe um número: '))
    numero2 = int(input('informe outro número: '))
    print(f'A soma dos numeros escolhidos é {numero1 + numero2}')
elif menu == 2:
    numero1 = int(input('informe um número: '))
    numero2 = int(input('informe outro número: '))
    if numero1 > numero2:
        print(f'A diferença entre os numeros é {numero1 - numero2}')
    else:
        print(f'A diferença entre os numeros é {numero2 - numero1}')
elif menu == 3:
    numero1 = int(input('informe um número: '))
    numero2 = int(input('informe outro número: '))
    print(f'O resultado é {numero1 * numero2}')
elif menu == 4:
    numero1 = int(input('informe o dividendo: '))
    numero2 = int(input('informe o divisor: '))
    print(f'O resultado da divisão é {numero1 / numero2}')
    if numero2 == 0:
        print('O denominador não pode ser zero')
else:
    print('Opção invalida')
