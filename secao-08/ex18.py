"""
18. Faça uma função que receba por parâmetro dois valores X e z. Calcule e retorneo
resultado de X^z para o programa principal. Atenção não utilize nenhuma função pronta
de exponenciação.

"""

def exp(x, z):
    return x ** z

x = int(input('Informe valor de x: '))
z = int(input('Informe valor de z: '))

print(exp(x, z))
