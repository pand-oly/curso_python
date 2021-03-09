"""
36. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e 
o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros números naturais é,

.         1² + 2² + ... + 10² = 385 

O quadrado da soma dos dez primeiros números naturais é,
.          (1 + 2 + ... + 10)² = 55² = 3025

A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025-385 = 2640.

"""
s = 0
quadrado = 0
for i in range(1, 101):
    s += (i ** 2)
    quadrado += i

q = quadrado ** 2
d = q - s
print(f'A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é {q}-{s} = {d}.')