"""
29. Faça um programa que receba 6 números inteiros e mostre:

• Os números pares digitados;
• A soma dos números pares digitados; 
• Os números ímpares digitados; 
• A quantidade de números ímpares digitados;

"""

vetor = []
pares = []
impares = []
for v in range(0, 6):
    num = int(input('Informe um número: '))
    vetor.append(num)

for i in vetor:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('Pares: ', pares)
print('Soma dos pares: ', sum(pares))
print('Impares: ', impares)
print('Quantidade de impares: ', len(impares))