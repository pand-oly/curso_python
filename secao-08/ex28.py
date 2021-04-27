"""
28. Faça uma função que receba como parâmetro o valor de um ângulo em graus e calcule
o valor do cosseno desse ângulo usando sua respectiva série de Taylor:

!formula

onde x é o valor do ângulo em radianos. Considerar = 3.141593 en variando de 0
até 5.

*devo aprender melhor série de tylor pra fazer essas questoes

"""

def fatorial(n):
    prod = 1
    for i in list(range(1, n + 1)):
        prod *= i
    return prod
 

def taylor_sin(ang):
    pi = 3.141593
    rad = ang * pi / 180
    coss = 1

    for n in range(6):
        coss += (-1) ** n * rad ** (2*n) / fatorial(2*n)

    return coss
 
 
ang = float(input('Ângulo (graus): '))
 
print(round(taylor_sin(ang), 2))