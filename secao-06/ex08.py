"""
8. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

"""

maior = -999
menor = 999
soma = 0

for i in range(1, 11):
    valor = int(input('Informe um valor: '))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f'Maior: {maior}')
print(f'Menor: {menor}')
