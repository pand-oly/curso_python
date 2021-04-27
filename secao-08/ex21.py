"""
21. Escreva uma função para determinar a quantidade de números primos abaixo N. 

"""

def contador(n):
    cont = 0
    for n in range(2, n + 1):
        if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
            cont += 1
        elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 and  n % 11 != 0:
            cont += 1
    
    return cont

n = int(input('Informe valor de N: '))
print(contador(n))
