"""
32. Faça uma função chamada 'simplifica' que recebe como parâmetro o numerador e o denominador
de uma fração. Esta função deve simplificar a fração recebida dividindo o numerador e o
denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplifica para 3/5 dividindo
o numerador e o denominador por 12. A função deve modificar as variáveis passadas como parâmetro.

"""

table2_20 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for n in range(2, 21):
    for i in range(1, 11):
        m = n * i
        table2_20[n-1].append(m)


def f(numerador, denominador):     
    for l in range(0, 10):
        if numerador in table2_20[l] and denominador in table2_20[l]:
           numer = table2_20[l].index(numerador) + 1
           denom = table2_20[l].index(denominador) + 1        
           
           return numer, denom


def primo(n, d):
    permissao = 'Divide mais'
    if (n == 2 or n == 3 or n == 5 or n == 7 or n == 11 and d == 2 or d == 3 or d == 5 or 
                        d == 7 or d == 11):
        permissao = 'fim,'
        return permissao
    elif (n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 and  n % 11 != 0 and 
                    d % 2 != 0 and d % 3 != 0 and d % 5 != 0 and d % 7 != 0 and  d % 11 != 0):
        permissao = 'fim,'
        return permissao
    
    return permissao


numer = int(input('Informe valor do numerdador: '))
denom = int(input('Informe valor do denominador: '))
print(numer,"/", denom)
numer, denom = f(numer, denom)
permissao = primo(numer, denom)
if permissao != 'fim,':
    numer, denom = f(numer, denom)

print(numer,"/", denom)
