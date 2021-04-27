"""
23. Escreva uma função que gera um triângulo lateral de altura 2*n-1 e n largura. Por exemplo,
a saída para n = 4 seria:

"""
def triangolo(n):
    for i in range(1, n):
        print('.' * i)
    for i in range(n, 0, -1):
        print('.' * i)


n = 4
triangolo(n)
