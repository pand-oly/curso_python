"""
4. Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y
quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma
dos valores encontrados nas respectivas posições X e Y.

"""

a = []
b = []
for vetor in range(1, 9):
    vetor = int(input('Informe número para o vetor A: '))
    a.append(vetor)

for vetor in range(1, 9):
    vetor = int(input('Informe número para o vetor B: '))
    b.append(vetor)

x = int(input('Informe valor para correspondente a X: '))
y = int(input('Informe valor para correspondente a Y: '))

soma = a[x] + b[y]
print(f'Soma dos valores na posição X e Y é {soma}')