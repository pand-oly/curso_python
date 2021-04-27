"""
37. Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o 
hiperfatorial desse número. O hiperfatorial de um número n, escrito (n), é definido por:
        n
H(n) = II=K^k = 1¹.2².3³... (n-1)^n-¹.n^n
        k

"""

def hiperfatorial(n):
    f = 1
    for k in range(1, n + 1):
        f *= k ** k
    
    return f

n = int(input('Digite um número: '))
print(hiperfatorial(n))
