"""
22. Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência 
arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente
média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa,
o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.

"""

nota = 10
s = 0
m = 0
while nota >= 10 and nota <= 20:
    nota = 0
    print('O programa sera fechado caso digite nota inferior a 10 ou superior a 20')
    nota = float(input('Digite a nota: '))
    if nota >= 10 and nota <= 20:
        s = nota + s
        m = m + 1

media = s / m
print(f'A media das notas fornecidas é {media}')
