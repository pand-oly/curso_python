"""
14. Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais
e os escreva na tela.

"""

vetor = []
for n in range(0, 10):
    num = int(input('Informe um número: '))
    vetor.append(num)

d = ''
for i in vetor:
    if vetor.count(i) > 1 and i != d:
        print(f'O número {i} aparece {vetor.count(i)} vezes na lista.')
        d = i
