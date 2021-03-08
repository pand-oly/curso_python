"""
18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o
maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.

"""

maior = -999
v = 0

q = int(input('Quantas vezes fazer a pergunta: '))

for i in range(1, q + 1):
    valor = int(input('Informe um valor: '))
    if valor >= maior:
        if valor > maior:
            maior = valor
            v = v * 0
        if valor == maior:
            v = v + 1

print(f'O numero maior {maior} apareceu {v} vezes.')