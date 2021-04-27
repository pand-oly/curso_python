"""
15. Leia uma matriz 5 x 10 que se refere respostas de 10 questões de múltipla escolha,
referentes a 5 alunos. Leia também um vetor de 10 posições contendo o gabarito de
respostas que podem ser (a, b, c, d, ou e). Seu programa deverá comparar as respostas
de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo
a pontuação correspondente a cada aluno.

"""

matriz = [[], [], [], [], []]

gabarito = ['a', 'd', 'a', 'b', 'c', 'c', 'c', 'a', 'd', 'd']

resultado = {'aluno 1': 0, 'aluno 2': 0, 'aluno 3': 0, 'aluno 4': 0, 'aluno 5': 0}


for aluno, corretas in resultado.items():

    print(f'\n\n-----\n{aluno.title()}:\n-----')


    for n in range(10):

        res = input(f'\nQuestão {n+1}: ').lower()


        while res != 'a' and res != 'b' and res != 'c' and res != 'd' and res != 'e':

            res = input(f'\nResposta inválida!\nRespota novamente questão {n+1}: ')

        if res == gabarito[n]:

            resultado[aluno] += 1


[print(f'\nO {a} respondeu {c} questões corretamente.') for a, c in resultado.items()]
