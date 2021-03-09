"""
43. Faça um programa que leia um número indeterminado de idades de indivíduos (pare
quando for informada a idade 0), e calcule a idade média desse grupo.

"""
soma = 0
media = 0
idade = int(input('Informe a idade: '))
while idade != 0:
    soma += idade
    if idade > 0:
        media += 1
    else:
        idade <= 0
        media -= 1
    idade = int(input('Informe a idade: '))

m = soma / media
print(f'A media deste grupo é {m}')
