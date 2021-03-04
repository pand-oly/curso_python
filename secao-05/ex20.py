"""
20. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isoscele, considerando os seguintes conceitos:

• O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados. 
• Chama-se equilátero o triângulo que tem três lados iguais. 
• Denominam-se isosceles o triângulo que tem o comprimento de dois lados iguais.
• Recebe o nome de escaleno o triângulo que tem os três lados diferentes. 

"""

a = int(input('Informe um numero: '))
b = int(input('Informe um numero: '))
c = int(input('Informe um numero: '))

if a > b + c or b > a + c or c > a + b:
    print('Invalido')
elif a == b and b == c:
    print('Equilátero')
elif a == b != c or a == c != b or b == c != a:
    print('Isosceles')
elif a != b and b != c:
    print('Escaleno')
