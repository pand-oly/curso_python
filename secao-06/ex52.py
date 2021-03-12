"""
52. Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e 
retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de 
notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.

"""

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

saque = int(input('Digite o valor que deseja sacar: '))

while saque >= 1:
    if saque >= 100:
        notas100 += 1
        saque -= 100
    elif saque >= 50:
        notas50 += 1
        saque -= 50
    elif saque >= 20:
        notas20 += 1
        saque -= 20
    elif saque >= 10:
        notas10 += 1
        saque -= 10
    elif saque >= 5:
        notas5 += 1
        saque -= 5
    elif saque >= 2:
        notas2 += 1
        saque -= 2
    elif saque >= 1:
        notas1 += 1
        saque -= 1

if notas100 > 0:
    print(f'{notas100} Notas de 100R$')
if notas50 > 0:
    print(f'{notas50} Notas de 50R$')
if notas20 > 0:
    print(f'{notas20} Notas de 20R$')
if notas10 > 0:
    print(f'{notas10} Notas de 10R$')
if notas5 > 0:
    print(f'{notas5} Notas de 5R$')
if notas2 > 0:
    print(f'{notas2} Notas de 2R$')
if notas1 > 0:
    print(f'{notas1} Notas de 1R$')
