"""
34. Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20? Ex: 2520 é o 
menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.

"""

numero = 1
 
while numero > 0:
    divisor = 1
    cont = 0
    while divisor <= 10:
        print(numero, divisor, cont)
        if numero % divisor == 0:
            cont += 1
        divisor += 1
    if cont == 20:
        break
    numero += 1
 
print(numero)
