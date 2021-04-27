"""
38. Faça uma função não-recursiva que receba um número inteiro positivo ne retorne o fatorial
exponencial desse número. Um fatorial exponencial é um inteiro positivo n elevado à potência
de n-1, que por sua vez é elevado à potência de n-2 e assim em diante. Ou seja:

N^(n-1)(n-2)...

"""

def exponencial(n):
    for e in range(n-1 , 0, -1):
        n = n ** e 
    
    return n

n = int(input('Digite um número: '))
print(exponencial(n))
