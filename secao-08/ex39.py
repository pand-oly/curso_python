"""
39. Faça uma função 'Troque', que recebe duas variáveis reais A e B e troca o valor delas
(i.e., A recebe o valor de B e B recebe o valor de A).

"""

def troque(a, b):
    i = a
    a = b
    b = i
    return a, b

a = int(input("Digite valor de A: "))
b = int(input("Digite valor de B: "))
a, b = troque(a, b)
print(f'A= {a} B= {b}')
