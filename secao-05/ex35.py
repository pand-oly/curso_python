"""
35. Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia 
existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.

"""

bissexto = False

data = int(input('informe a data: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        bissexto = True

if mes == 1:
      if data >= 1 and data <= 31:
        print('Data valida')
elif mes == 2:
    if bissexto is True:
        if data >= 1 and data <= 29:
            print('Data valida')
        else:
            print('Data invalida')
    elif bissexto is False:
        if data >= 1 and data <= 28:
            print('Data valida')
        else:
            print('Data invalida')
elif mes == 3:
    if data >= 1 and data <= 31:
        print('Data valida')
elif mes == 4:
    if data >= 1 and data <= 30:
        print('Data valida')
elif mes == 5:
    if data >= 1 and data <= 31:
        print('Data valida')
elif mes == 6:
    if data >= 1 and data <= 30:
        print('Data valida')
elif mes == 7:
    if data >= 1 and data <= 31:
        print('Data valida')
elif mes == 8:
    if data >= 1 and data <= 31:
        print('Data valida')
elif mes == 9:
    if data >= 1 and data <= 30:
        print('Data valida')
elif mes == 10:
    if data >= 1 and data <= 31:
        print('Data valida')
elif mes == 11:
    if data >= 1 and data <= 30:
        print('Data valida')
elif mes == 12:
    if data >= 1 and data <= 31:
        print('Data valida')
else:
    print('Data invalida')
