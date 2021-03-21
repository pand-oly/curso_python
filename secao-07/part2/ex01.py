"""
1. Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.

"""
'''
# !forma 1 de fazer matrizes  # way 1 to make that matrix
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'[{l}, {c}]: '))
print('-=' * 30)
#! format quadrado --- adc forma de matriz
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^2}]', end='')
    print()

#* Ps. Gustavo Guanabara - curso em video
'''


# forma 2  #* Aprendi olhando codigo do Guanabara e fiz com conhecimento que tenho ate agora vindo do curso da geek

matriz = [[], [], [], []]
for l in range(0, 4):
    for c in range(0, 4):
        num = int(input(f'Digite para posição [{l}, {c}]: '))
        matriz[l].append(num)
print('')
print('-=' * 30)
print('')
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()

cont = 0
for IL in range(len(matriz)):              #* Il- index linha
    for IC in range(len(matriz[IL])):      #* IC- index coluna
        if matriz[IL][IC] > 10:            #* abreviação maiuscula estva mais facil de ler
            cont += 1

print(f'Há {cont} números maiores que 10')
print('Suas posições:')

for IL in range(len(matriz)):
    for IC in range(len(matriz[IL])):
        if matriz[IL][IC] > 10:
            AbrevIIL = matriz.index(matriz[IL])
            AbrevIIC = matriz.index(matriz[IC])
            n = matriz[IL][IC]             #! Abreviar para o  print não ficar tão grande
            print(f"""Na linha {AbrevIIL} coluna {AbrevIIC} esta o numero {n}""")
