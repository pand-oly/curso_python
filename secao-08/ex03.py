"""
3. Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor
de retorno será 1 se positivo, -1 se negativo e o se for igual a 0.

"""

def verif(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0

num = int(input('Informe o número: '))

print(verif(num))
