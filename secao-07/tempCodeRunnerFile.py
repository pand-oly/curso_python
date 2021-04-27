#matriz = 1 + x, 2 + x, 3 + x, 6 + x, 4 + x, 5 + x, 7 + x, 8 + x, 9 + x, 0 + x
#         1 + x, 2 + x, 3 + x, 4 + x, 5 + x, 6 + x, 7 + x, 8 + x, 9 + x, 0 + x
#         1 + x, 2 + x, 3 + x, 4 + x, 5 + x, 6 + x, 7 + x, 8 + x, 9 + x, 0 + x
#         1 + x, 2 + x, 3 + x, 4 + x, 5 + x, 6 + x, 7 + x, 8 + x, 9 + x, 0 + x
#         1 + x, 2 + x, 3 + x, 4 + x, 5 + x, 6 + x, 7 + x, 8 + x, 9 + x, 0 + x

# vetor = [1x, 2x, 3x, 4x, 5x, 6x, 7x, 8x, 9x, 0x]

vetor = [[1, 2, 3, 4], [5, 6, 7]]
gab = {}
l = 0
for i in range(len(vetor[l])):
    if i == 0:
        gab['a'] = vetor[l][i]
    elif i == 1:
        gab['b'] = vetor[l][i]
    elif i == 2:
        gab['c'] = vetor[l][i]
    elif i == 3:
        gab['d'] = vetor[l][i]
    elif i == 4:
        gab['e'] = vetor[l][i]
print(gab)

matriz = [['1+1', '2+3', '2+2'], ['1+1', '2+3', '2+2'], ['1+1', '2+3', '2+2']]
resposta = [[], [], [], [], []]
for aluno in range(0, 2):
    for questao in range(0, 3):
        pergunta = int(input(f'{matriz[aluno][questao]} = '))
        resposta[aluno].append(pergunta)
    print('-=' * 10)
print(resposta)


for r in range(len(resposta[0])):
    if resposta[0][r] == vetor[0][1]:
        print('S')
    else:
        print('q')
    print(resposta[0])