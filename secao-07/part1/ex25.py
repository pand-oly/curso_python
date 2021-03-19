"""
25. Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que
não são múltiplos de 7 ou que terminam com 7.

"""

vetor = []
num = 1
while len(vetor) < 100:
    for i in str(num):
        i = int(i)
    if num % 7 != 0 and i != 7:
        vetor.append(num)
    
    num += 1

print(vetor)