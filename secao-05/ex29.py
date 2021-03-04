"""
29. Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do 
que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde 
a e b são os números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as 
perguntas e as respostas corretas, além de quantas vezes o aluno acertou.

"""


from random import *

vetor = []
correto = 0

for i in range(0, 5):
    a = randint(1,100)
    vetor.append(a)
    b = randint(1,100)
    vetor.append(b)
    s = a + b
    p = int(input(f'Quanto é {a} + {b} = '))
    if p == s:
        correto = correto + 1
        print('Correto')
    else:
        print('Incorreto')
print(f'Acertou {correto} das 5 perguntas')
