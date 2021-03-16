"""
5. Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui. 

"""

print('Dgite 10 numeros para o vetor')
a = []
cont = 0
c = 0
for vetor in range(0, 10):
    c += 1
    num = int(input(f'{c}° Digite um número para vetor: '))
    a.append(num)

for i in a:
    if i % 2 == 0:
        cont += 1

print(f'Em um vetor com {c} numeros {cont} são pares')