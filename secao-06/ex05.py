"""
5. Faça um programa que peça ao usuário para digitar 10 valores e some-os. 

"""
vetor = []
soma = 0
for i in range(0, 10):
    numb = int(input('Digite um valor: '))
    vetor.append(numb)
    soma = soma + numb
print(f'soma: {soma}')