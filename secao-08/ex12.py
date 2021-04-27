"""
12. Escreva uma função que receba um número inteiro maior do que zero e retorne a soma de todos
os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número
lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".

"""


def soma(numero):
    soma = 0
    for n in numero:
        n = int(n)
        soma += n
    return soma

numero = input('Informe um número: ')
print(soma(numero))