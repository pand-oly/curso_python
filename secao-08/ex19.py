"""
19. Faça uma função que retorne o maior fator primo de um número.

"""

def primo(num):
    for n in range(2, num + 1):
        if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
            ultimop = n
        elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 and  n % 11 != 0:
            ultimo = n
    
    return ultimo

num = int(input('Informe um número: '))
print(primo(num))
