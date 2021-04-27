"""
70. Um racional é qualquer número da forma p/q, sendo p inteiro e q inteiro não nulo. É
conveniente representar um racional por um registro:

struct racional{
    int p, q;
};

Vamos convencionar que o campo q de todo racional é estritamente positivo e que o máximo divisor
comum dos campos p e q é 1. Escreva

(a) uma função reduz que receba inteiros a e b e devolva o racional que representa a/b;

(b) uma função neg que receba um racional x e devolva o racional - x;

(c) uma função soma que receba racionais x e y e devolva o racional que representa a soma de x e y;

(d) uma função mult que receba racionais x e y e devolva o racional que representa o
produto de x por y;

(e) uma função div que receba racionais x e y e devolva o racional que representa o
quociente de x por y;

"""

def p_q():
    p = int(input('Digite um número: '))
    q = 0
    while q == 0:
        q = int(input('Digite outro número != de 0: '))

    return p, q

p, q = p_q()

def reduz():
    a = int(input('Digite um número: '))
    b = 0
    while b == 0:
        b = int(input('Digite outro número != de 0: '))
    
    print('(a): ', a/b)

reduz()


def neg():
    x = int(input('Digite um número positivo: '))
    print('(b): ', x * -1 )

neg()


def soma():
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    print('(c): ', x + y)

soma()


def mult():
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    print('(d): ', x * y)

mult()


def div():
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    print('(e): ', x / y)

div()
