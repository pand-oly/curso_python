"""
5. Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca desse valor
na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de
"não encontrado".

"""

matriz = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 'x', 4, 5]]

for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]}]', end='')
    print()

permissao = False
for l in range(0, 5):
    for c in range(0, 5):
        if matriz[l][c] == 'x':
            print(f'Encontrado posição [{l},{c}] ')
            permissao = True
        else:
            permissao = False

        if permissao == True:
            break
            
if permissao == False:
    print('Não encontrado')