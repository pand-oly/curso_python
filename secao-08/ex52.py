"""
52. Escreva uma função que recebe uma matriz quadrada de ordem N e calcule a sua transposta
(se B é a matriz transposta de A então aij = bji).

"""

matriz = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
def ordem_n(matriz):
    for l in range(4):
        for c in range(4):
            print(f'[{matriz[l][c]}]', end='')
        print()

ordem_n(matriz)

print('\n', '=-'*30, '\n')

def ordem_t(matriz):
    transposta = [[], [], [], []]
    for l in range(4):
        for c in range(4):
            if l == l:
                transposta[l].append(matriz[c][l])
    
    for l in range(4):
        for c in range(4):
            print(f'[{transposta[l][c]}]', end='')
        print()

ordem_t(matriz)
