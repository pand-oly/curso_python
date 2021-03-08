"""
27. Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmónica:

H(n) = 1+1/2+1/3+1/4+ ... +1/n 

Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).

"""

H_n = int(input('Informe número para H(n) de inicio '))
H_n_f = int(input('Informe número para H(n) final '))
m = 0
d = 0
for i in range(H_n, H_n_f + 1):
    d = (1 / i) + d
    m = m + 1

h = m / d
print(h)