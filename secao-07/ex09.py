"""
9. Crie um programa que le 6 valores inteiros pares e, em seguida, mostre na tela os valores
lidos na ordem inversa.

"""

vetor = []
for i in range(0, 6):
    num = int(input('Informe um número par: '))
    if num % 2 == 0:
        vetor.append(num)
    else:
        print('Número tem que ser par ')
        num = int(input('Informe um número par: '))
    
print(vetor[::-1])
