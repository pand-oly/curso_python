"""
16. Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código
inteiro. Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta;
se for 2, mostre o vetor na ordem inversa. Caso, o código for diferente de 1 e 2 escreva uma
mensagem informando que o código é inválido.

"""
vetor = []
for n in range(0, 5):
    num = float(input('Informe um número: '))
    vetor.append(num)

p = int(input('Digite 1 ou 2 para execuclção: '))

if p == 1:
    print(vetor)
elif p == 2:
    print(vetor[::-1])
else:
    p != 1 and p != 2
    print('código é inválido.')