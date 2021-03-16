"""
11. Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a
quantidade de números negativos e a soma dos números positivos desse vetor.

"""

vetor = []
for i in range(0, 10):
    num = int(input('Informe um valor: '))
    vetor.append(num)

index = len(vetor)
cont = 0
soma = 0
for c in range(0, index):
    if vetor[c] < 0:
        cont += 1
    else:
        vetor[c] > 0
        soma += vetor[c]

print(f'Você digitou {cont} números negativos')
print('Esta é a soma dos positivos: ', soma)
