"""
33. Dados n e dois números inteiros positivos, i ej, diferentes de O, imprimir em ordem crescente os n
primeiros naturais que são múltiplos de i ou de je ou de ambos. Exemplo: Para n = 6, i = 2 e j = 3 a saída 
deverá ser: 0,2,3,4,6,8.

"""

q = int(input('Informe valor de n: '))
i = int(input('Informe valor de i: '))
j = int(input('Informe valor de j: '))
for n in range(1, q + 1):
    if n % i == 0:
        print(f'{n}', end=', ')
    if n % j == 0:
        print(n, end=', ')