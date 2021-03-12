"""
50. Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centímetros
por ano. Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que
Chico.

"""

chico = 1.50
ze = 1.10
cont = 0
while ze < chico:
    chico += 0.02
    ze += 0.03
    cont += 1

print(f'Com {cont} meses ze alcancara chico')
print(f'Altura de zé daqui a {cont} Anos será {"%.2f" % ze}')
print(f'E chico vai ter {"%.2f" % chico} ')
