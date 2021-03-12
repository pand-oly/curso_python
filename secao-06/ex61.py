"""
61. Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois
números de 3 dígitos. Ex: O maior palíndromo feito a partir do produto de dois números de dois
dígitos é 9009 = 91*99.

"""

maior = 0
for n1 in range(100, 1000):
    for n2 in range(100, n1):
        nunb = n1 * n2
        string = str(nunb)
        inverso = string[::-1]

        if string == inverso:
            string = int(string)
            inverso = int(inverso)
            if inverso > maior:
                maior = inverso

print(maior)