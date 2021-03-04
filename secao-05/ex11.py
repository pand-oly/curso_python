"""
11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".

"""

numero = int(input('Digite um número inteiro: '))
q = 0

if numero >= 0:
    for c in str(numero):
        q = q + int(c)
    print(f'A soma dos números é {q}')
else:
    print('Número invalido')
