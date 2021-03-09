"""
41. Faça um programa que calcula a associação em  paralelo de dois resistores R1 e R2 fornecidos pelo usuário
via teclado. O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para 
resistência igual a zero.

R = R1 * R2
    R1 + R2

"""

r1 = int(input('Informe valor de R1: '))
r2 = int(input('Informe valor de R2: '))

while r1 > 0 and r2 > 0:
    r = (r1 * r2) / (r1 + r2)
    print(r)
    r1 = int(input('Informe valor de R1: '))
    r2 = int(input('Informe valor de R2: '))
