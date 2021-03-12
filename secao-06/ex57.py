"""
57. Faça um programa que conte quantos números primos existem entre A e B, onde A e B
são números informados pelo usuário.

"""
print('A e B devem ser maiores que 1')
a = 0
b = 0
while a <= 1:
    a = int(input('Informe valor de A: '))
while b <= 1:
    b = int(input('Informe valor de B: '))
cont = 0

for i in range(a, b + 1):
    if i == 2 or i == 3 or i == 5 or i == 7 or i == 11:
        cont += 1
    elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and  i % 11 != 0:
        cont += 1

print(f'Tem {cont} números primos entre A e B')
