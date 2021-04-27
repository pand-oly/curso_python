"""
44. Faça uma função que receba como parâmetro um vetor X de 30 elementos inteiros e
retorne, também por parâmetro, dois vetores A e B. O vetor A deve conter os elementos
pares de X e o vetor B, os elementos ímpares.

"""

def vetor(x):
    a = []
    b = []
    for n in x:
        if n % 2 == 0:
            a.append(n)
        else:
            b.append(n)

    return f'A{a} \nB {b}'


x = list(range(30))
print(vetor(x))
