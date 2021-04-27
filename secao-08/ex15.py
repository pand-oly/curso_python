"""
15. Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando
as medidas dos três lados de um triângulo. Elabore funções para:

(a) Determinar se eles lados formam um triângulo, sabendo que:
        • O comprimento de cada lado de um triângulo é menor do que a soma dos outros
        dois lados.
(b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo.
Sendo que:
        • Chama-se equilátero o triângulo que tem três lados iguais.
        • Denominam-se isosceles o triângulo que tem o comprimento de dois lados iguais. 
        • Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

"""

l1 = 0
l2 = 0
l3 = 0
while l1 <= 0:
    l1 = int(input('Informe um número maior que 0: '))
while l2 <= 0:
    l2 = int(input('Informe um número maior que 0: '))
while l3 <= 0:
    l3 = int(input('Informe um número maior que 0: '))

def a(l1, l2, l3):
    if l1 > (l2 + l3):
        return 'Não é um triângulo'
    elif l2 > (l1 + l3):
        return 'Não é um triângulo'
    elif l3 > (l2 + l1):
        return 'Não é um triângulo'
    else:
        return 'É um triângulo'

def b(l1, l2, l3):
    if l1 == l2 and l1 == l3:
        return 'Triângulo equilátero'
    elif l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l3 == l2 and l2 != l1:
        return 'Triângulo isosceles'
    elif l1 != l2 and l2 != l3 and l1 != l3:
        return 'Triângulo escaleno'

print(a(l1, l2, l3))
print(b(l1, l2, l3))
