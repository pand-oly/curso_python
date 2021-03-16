"""
20. Escreva um programa que leia números inteiros no intervalo [0,50) e os armazene em um
vetor com 10 posições. Preencha um segundo vetor apenas com os números ímpares do primeiro
vetor. Imprima os dois vetores, 2 elementos por linha. 

"""
n = int(input('Informe um número: '))
vetor = []
for v in range(0, 10):
    n += 0.5
    vetor.append(n)

print(vetor)

impares = []
for i in vetor:
    if i % 2 != 0:
        impares.append(i)
    
print(impares)

# não sei qual da duas estão certas

n = int(input('Informe um nmero: '))
vetor = []
for v in range(0, 10):
    n += 0.5
    vetor.append(int(n))

print(vetor)

impares = []
for i in vetor:
    if i % 2 != 0:
        impares.append(i)
    
print(impares)