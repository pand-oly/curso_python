"""
38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano. 
Teste a validade desta data para saber se esta é uma data válida. Teste se o dia fornecido é um dia válido:
dia > 0, dia <28 para o mês de fevereiro (29 se o ano for bissexto), dia < 30 em abril, junho, setembro e
novembro, dia < 31 nos outros meses. Teste a validade do mês: mês > O e mês < 13. Teste a validade do ano:
ano ano atual (use uma constante definida com o valor igual a 2008). Imprimir: "data válida" ou "data 
inválida" no final da execução do programa.

"""
bissexto = False

data = input("Informe dia de nacimento: dd/mm/yyyy ")

dia,mes,ano = data.split("/") # Separando o dia dos meses e ano
dia = int(dia)
mes = int(mes)
ano = int(ano)

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        bissexto = True

if mes == 1:
      if dia >= 1 and dia <= 31:
        print('Data valida')
      else:
        print('Data invalida')
elif mes == 2:
    if bissexto is True:
        if dia >= 1 and dia <= 29:
            print('Data valida')
        else:
            print('Data invalida')
    elif bissexto is False:
        if dia >= 1 and dia <= 28:
            print('Data valida')
        else:
            print('Data invalida')
elif mes == 3:
    if dia >= 1 and dia <= 31:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 4:
    if dia >= 1 and dia <= 30:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 5:
    if dia >= 1 and dia <= 31:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 6:
    if dia >= 1 and dia <= 30:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 7:
    if dia >= 1 and dia <= 31:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 8:
    if dia >= 1 and dia <= 31:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 9:
    if dia >= 1 and dia <= 30:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 10:
    if dia >= 1 and dia <= 31:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 11:
    if dia >= 1 and dia <= 30:
        print('Data valida')
    else:
        print('Data invalida')
elif mes == 12:
    if dia >= 1 and dia <= 31:
        print('Data valida')
    else:
        print('Data invalida')
else:
    print('Data invalida')
