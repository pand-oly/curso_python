"""
37. Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade 
seguinte: a soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao 
quadrado é igual ao próprio numero. Por exemplo, para o inteiro 3025, temos que: 30+ 25 = 55 552 = 3025

"""

for c in range(1000, 10000):
    w = str(c)
    x = w[0:2]
    y = w[2:]
    z = int(x) + int(y)
    if z ** 2 == c:
        print(c)
