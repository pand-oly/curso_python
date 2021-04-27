"""
58. Faça uma função que receba, por parâmetro, duas matrizes quadradas de orden N, A e
B, e retorna uma matriz C, também por parâmetro, que seja o produto matricial de A e B.

"""

a = [[1, 2, 3], [1, 4, 3], [1, 7, -3]]
b = [[4, 5, 6], [4, 5, -6], [-2, 5, 5]]

def matriz_c(a, b):
    c = []
    for i in range(len(b)):  #numero de linas que vão ser criadas para matriz C
        c.append([])

    for l in range(len(a)):
        i = 0
        j = 0
        for k in range(len(a[l])):
            n = a[l][k] * b[i][j]
            c[l].append(n)
            i += 1
        j += 1
    
    return c

c = matriz_c(a, b)

def ordenar(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz)):
            print(f'[{matriz[l][c]:2}]', end='')
        print()


print('A')
ordenar((a))
print('\nB')
ordenar((b))
print('\nC')
ordenar((c))
