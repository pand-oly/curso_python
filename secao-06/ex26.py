"""
26. Faca um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.

"""

numero = int(input('Informe um numero: '))
numero2 = numero + 1000
onze = 0
treze = 0
deze7 = 0
for i in range(numero, numero2):
    if i % 11 == 0:
        onze = i
    if i % 13 == 0:
        treze = i
    if i % 17 == 0:
        deze7 = i
    if onze and treze and deze7 > 0:
        break

print(onze,
treze,
deze7)