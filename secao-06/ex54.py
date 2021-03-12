"""
54. Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é
primo ou não.

"""
n = int(input('Informe um valor > 1: '))
d = n
u = 1

if n > 1:
    for i in range(2, n):
        if n % u == 0 and n % d == 0 and n % i != 0:
            resposta = True
        elif n % i == 0:
            resposta = False
            break

    if resposta is True:
        print(f'O número {n} é Primo')
    else:
        print(f'O número {n} não é Primo')
else:
    print('O numero devera ser maior que 1:')
