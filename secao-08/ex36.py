"""
36. Faça uma função não-recursiva que receba um número inteiro positivo N e retorneo
superfatorial desse número. O superfatorial de um número N é definida pelo produto dos N
primeiros fatoriais de N. Assim, o superfatorial de 4 é sf(4) = 1! * 2! * 3! * 4! = 288.

"""

def super_fatorial(numero):
    sf = 1
    for fatorial in range(1, numero+1):
        f = 1
        for n in range(fatorial, 0, -1):
            f *= n
        
        sf *= f
    
    return sf

numero = int(input('Informe um número: '))
print(super_fatorial(numero))
