"""
12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número
inválido". Se o número for positivo, calcular o logaritmo deste numero.

"""

numero = int(input('Informe um número: '))
i = 0

if numero < 0:
    print('Número inválido')
else:
    for c in str(numero):
        i = i + int(c)
    print(i)
