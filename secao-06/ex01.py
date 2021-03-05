"""
1. Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, conside
rando números maiores que 0.

"""

for i in range(0, 26): 
    if i % 3 == 0:
        if i > 0 and i <= (3 * 5):
            print(f'P número {i} é multiplo de 3')