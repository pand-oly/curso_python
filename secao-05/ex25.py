"""
25. Calcule as raízes da equação de 2o grau:

                   Lembrando que:

                            x = -b +/- √Δ
                                    2a

                                   Onde
                                Δ = B² - 4ac
                E 'Ax² + Bx + c = 0' representa uma equação de 2° grau.

A variável 'a' tem que ser diferente de zero. Caso seja igual, imprima a 
mensagem "Não é equação de segundo grau".

• Se D < 0, não existe real. Imprima a mensagem Não existe raiz. 
• Se D = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única. 
• Se D > 0, imprima as duas raízes reais.

"""

print('Lembrando que:  Ax² + Bx + c = 0  Informe:')
a = int(input('A = '))
b = int(input('B = '))
c = int(input('C = '))

if a == 0:
    print("Não é equação de segundo grau")
else:
    d = b ** 2 -4 * a * c
    if d < 0:
        print('Não existe raiz')
    elif d == 0:
        x = -b / (2 * a)
        print(f'x = {x} "Raiz única"')
    elif d > 0:
        raiz = d ** 0.5
        x1s = -b + raiz 
        x1 = x1s / (2 * a)
        x2s = -b - raiz
        x2 = x2s / (2 * a)
        print(f'x1 = {x1} e x2 = {x2}')
