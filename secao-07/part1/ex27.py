"""
27. Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos
que são primos e suas respectivas posições no vetor.

"""

vetor = []
for v in range(0, 10):
    num = int(input('Digite um número para o primeiro vetor: '))
    vetor.append(num)

for v in vetor:
    if v == 2 or v == 3 or v == 5 or v == 7 or v == 11:
        index = vetor.index(v)
        print(f'{v} é primo esta na posição {index}')
    elif v % 2 != 0 and v % 3 != 0 and v % 5 != 0 and v % 7 != 0 and  v % 11 != 0:
        index = vetor.index(v)
        print(f'{v} é primo esta na posição {index}')
