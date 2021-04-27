"""
12. Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e o 
número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre no arquivo 
(ignorando letras com acento). Obs.: palavras são separadas por um ou mais caracteres espaço,
tabulação ou nova linha.

"""

def linhas():
    with open('ex12-file.txt', 'r') as arq:
        print(f'Arquivo tem {len(arq.readlines())} linhas')


def palavras():
    with open('ex12-file.txt', 'r') as arq:
        palavras = arq.read().split('\n')
        new = []
        for p in palavras:
            palavra = p.split(' ' or ',' or '.' or '-' or '_')
            for i in palavra:
                new.append(i)
        
        print(f'Arquivo tem {len(new)} palavras')

def letras():
    alfabeto = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    with open('ex12-file.txt', 'r') as fil:
        for i in fil.read():
            if i.lower() in alfabeto:
                alfabeto[i.lower()] += 1
    
    print(alfabeto)

linhas()
palavras()
letras()
