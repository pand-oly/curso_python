"""
 10.Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.

"""
soma = 0
for i in range(0, 101):
    if i % 2 == 0:
        soma = soma + i

print(soma)