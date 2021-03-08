"""
21. Faça um programa que receba dois números. Calcule e mostre:

• a soma dos números pares desse intervalo de números, incluindo os números digitados;
. a multiplicação dos números ímpares desse intervalo, incluindo os digitados;

"""

inicio = int(input('Informe o numero de inicio do programa:'))
fim = int(input('Informe o numero de fim do programa:'))
s = 0
m = 1
for i in range(inicio, fim + 1):
    if i % 2 == 0:
        s = s + i
    else:
        m = m * i
    
print(f'Soma: {s}')
print(f'Mul: {m}')
