"""
24. Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1. Por exemplo,
a saída para n = 6 seria:

     *
    ***
   *****
  *******
 *********
***********

"""

def triangolo(n):
    q = 1
    for i in range(1, n + 1):
        print(' '* n, '1' * q)
        n -= 1
        q += 2
    
n = int(input('Informe o valor de n: '))
triangolo(n)