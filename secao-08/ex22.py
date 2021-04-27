"""
22. Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com
pontos de exclamação, conforme o exemplo abaixo (para n = 5):

!
!!
!!!
!!!!
!!!!!

"""

def triangolo(n):
    for i in range(1, n + 1):
        print('!' * i)

n = 5
triangolo(n)
