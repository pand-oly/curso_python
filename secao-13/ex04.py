"""
4. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas
letras são vogais e quantas são consoantes.

"""

fil = input('Digite nome do aquivo: ')

numeros = [str(numero) for numero in range(0,1000)]
vogais = ['a','e', 'i', 'o', 'u']

with open(fil, 'r') as fil:
    cont_Vogais = 0
    cont_Consoants = 0
    for i in fil.read():
        if i.lower() in vogais:
            cont_Vogais += 1
        elif i.lower() not in numeros and i.lower() != ' ' and i.lower() != '\n':
            cont_Consoants += 1
            
print(f'tem {cont_Vogais} vogais')
print(f'tem {cont_Consoants} consoantes')
