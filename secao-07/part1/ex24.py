"""
24. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número
do aluno e o segundo representando a sua altura em metros. Encontre o aluno mais baixo e o mais
alto. Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.

"""
chamada = []
altura = []
for v in range(0, 5):
    num = int(input('\nInforme número da cahamada do aluno: '))
    chamada.append(num)
    h = float(input('Informe altura deste aluno : '))
    altura.append(h)

IndexMin = altura.index(min(altura))
IndexMax = altura.index(max(altura))

print(f'\nMenor aluno: {chamada[IndexMin]} sua Altura: {altura[IndexMin]} ')
print(f'Maior aluno: {chamada[IndexMax]} sua Altura: {altura[IndexMax]} ')
"""
for i in range(0, 5):
    print(f'Aluno: {chamada[i]} sua Altura: {altura[i]} ')
    """