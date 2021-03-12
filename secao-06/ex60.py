"""
60. Faça um programa que leia vários números, calcule e mostre: (a) A soma dos números
digitados (b) A quantidade de números digitados (c) A média dos números digitados
(d) O maior número digitado (e) O menor número digitado (f) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0.

"""

a = 0
b = 1
s = 0
maior = -999
menor = 999
par = 0
m = 0

print('Para parar o programa Digite 0')
n = int(input('Digite um numero: '))

while n != 0:
    a = n
    s += n
    if n % 2 == 0 and n != 0:
        par += n
        m += 1

    b += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n

    n = int(input('Digite outro numero: '))
    if n == 0:
        break
    
    a += n
    print(f'(A) Soma de dois numeros {a}')

c = s / b
f = par / m
print(f'(B) {b} números foram digitados')
print(f'(C) A media é {"%.2f" % c}')
print(f'(D) O maior é {maior}')
print(f'(E) O menor é {menor}')
print(f'(F) A media dos numeros pares {"%.2f" % f}')