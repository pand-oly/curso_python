"""
12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a média dos valores.

"""

vetor = []
for i in range(0, 5):
    num = int(input('Informe um número: '))
    vetor.append(num)

print('Maior', max(vetor))
print('Menor', min(vetor))
print('Media', sum(vetor) / (i + 1))