"""
6. Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá
ser impresso o maior e o menor elemento do vetor.

"""

print('Dgite 10 numeros para o vetor')
a = []
c = 0
for vetor in range(0, 10):
    c += 1
    num = int(input(f'{c}° Digite um número para vetor: '))
    a.append(num)

print('Maior número: ', max(a))
print('Menor número: ', min(a))