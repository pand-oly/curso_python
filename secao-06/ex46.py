"""
46. Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o número 
foi gerado, a cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O 
programa acaba quando o usuário acerta o número gerado. O programa deve informar em quantas tentativas o 
número foi descoberto.

"""

vetor = []
errou = 0
from random import *
n = randint(1,10)
vetor.append(n)
resposta = int(input('tente adivinhar o numero de 1 a 1000: '))
if resposta == n:
    print('Acertou de 1°')
else:
    while n != resposta:
        if resposta > n:
            print('Maior')
            errou += 1
        elif resposta < n:
            print('Menor')
            errou += 1
        else:
            resposta == n
            break
        
        n = randint(1,10)
        vetor.append(n)
        resposta = int(input('tente adivinhar o numero de 1 a 1000: '))

    print(f'Acertou!!\nFim do Programa.... Você errou {errou} Vezes')
