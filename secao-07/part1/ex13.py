"""
13. Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram
o maior e o menor valor.

"""


vetor = []
for i in range(0, 5):
    num = int(input('Informe um número: '))

print('A posição do numero maior é: ', vetor.index(max(vetor)))
print('A posição do numero menor é: ', vetor.index(min(vetor)))