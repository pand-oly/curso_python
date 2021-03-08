"""
19. Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída
cada um dos algarismos que compõem o número 

"""

numero = 0

while numero < 100 or numero > 999:
    numero = int(input('Informe um número de 100 a 999: '))
    for c in str(numero):
        print(c)

 