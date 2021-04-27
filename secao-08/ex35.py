"""
35. Faça uma função não-recursiva que receba um número inteiro positivo ne retorne o fatorial
quádruplo desse número. O fatorial quádruplo de um número n é dado por:
(2n)!
  n!

"""

def fatorial_quaduplo(num1, num2):
    f1 = 1
    for n in range(num1, 0, -1):
        f1 *= n
    
    f2 = 1
    for n in range(num2, 0, -1):
        f2 *= n
    
    f = f1 // f2
    return f


numero = int(input('Informe um número: '))
print(fatorial_quaduplo(numero * 2, numero))
