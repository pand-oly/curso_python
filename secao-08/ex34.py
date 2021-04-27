"""
34. Faça uma função não-recursiva que receba um número inteiro positivo impar Ne retorne o
fatorial duplo desse número. O fatorial duplo é definido como o produto de todos os números
naturais ímpares de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é:
5!! = 1 *3 * 5 = 15

"""

def fatorial_duplo(n):
    calculo = 1
    for i in range(1, n+1):
        if i % 2 != 0:
            calculo *= i
        
    return calculo

n = 0
while n % 2 == 0:
    n = int(input('Digite um número: '))
print(fatorial_duplo(n))
