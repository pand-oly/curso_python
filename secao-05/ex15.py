"""
15. Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

! switch  ????

"""

num = int(input("Informe o numero referente o dia da semana: "))

if num == 1:
    print("Domingo")
elif num == 2:
    print("Segunda-Feira")
elif num == 3:
    print("Terça-Feira")
elif num == 4:
    print("Quarta-Feira")
elif num == 5:
    print("Quinta-Feira")
elif num == 6:
    print("Sexta-Feira")
elif num == 7:
    print("Sábado")
else:
    print("Número Inválido")
