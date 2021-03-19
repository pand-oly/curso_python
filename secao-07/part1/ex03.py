"""
3. Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes
deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada.
Imprimir todos os conjuntos.

"""

a = []
b = []
for i in range(1, 11):
    num = int(input('informe um número: '))
    a.append(num)

for x in a:
    q = x ** 2
    b.append(q)

print(b)
