"""
73. Foi realizada um pesquisa de algumas características físicas de cinco habitantes de certa
região. De cada habitante foram coletados os seguintes dados: sexo, cor dos olhos (A - Azuis ou 
C - Castanhos), cor dos cabelos (L - Louros, P- Pretos ou C- Castanhos) e idade.

• Faça uma função que leia esses dados em um vetor.

• Faça uma função que determine a média de idade das pessoas com olhos castanhos e cabelos pretos.

• Faça uma função que determine e devolva ao programa principal a maior idade entre os habitantes.

• Faça uma função que determine e devolva ao programa principal a quantidade de indivíduos do sexo
feminino cuja idade está entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros.

"""

def dados(**kwargs):
    vetor = dict()
    vetor.update(kwargs)
    
    return vetor

def pesquisa():
    genero = input('Informe o genero M.para Masculino, F.para Feminino: ').upper()
    idade = int(input('Informe a idade: '))
    olhos = input('Digite "A" - para olhos Azuis ou "C" - para olhos Castanhos ').upper()
    cabelos = input('Digite "L" - para cabelos Loiros, "C" - para Castanhos ou "P" para cabelos pretos ').upper()
    
    return dados(genero= genero, idade=idade, olhos=olhos, cabelos= cabelos)


def media(h1,h2,h3,h4,h5):
    cabelo = h1['cabelo'], h2['cabelo'], h3['cabelo'], h4['cabelo'], h5['cabelo']
    olhos = h1['olhos'], h2['olhos'], h3['olhos'], h4['olhos'], h5['olhos']
    idade = h1['idade'], h2['idade'], h3['idade'], h4['idade'], h5['idade']
    soma = 0
    divisor = 0
    for i in range(5):
        if cabelo[i].upper() == 'P' and olhos[i].upper() == 'C':
            soma += idade[i]
            divisor += 1
    
    m = soma / divisor

    return m

def mais_velho(idade):
    return idade.index(max(idade))


def interesseiro(h1, h2, h3, h4, h5):
    cabelo = h1['cabelo'], h2['cabelo'], h3['cabelo'], h4['cabelo'], h5['cabelo']
    olhos = h1['olhos'], h2['olhos'], h3['olhos'], h4['olhos'], h5['olhos']
    idade = h1['idade'], h2['idade'], h3['idade'], h4['idade'], h5['idade']
    genero = h1['genero'], h2['genero'], h3['genero'], h4['genero'], h5['genero']
    cont = 0
    for i in range(5):
        if genero[i] == 'F':
            if idade[i] >= 18 and idade[i] <= 35:
                 if cabelo[i] == 'L' and olhos[i] == 'A':
                     cont += 1

    return cont


h1 = pesquisa()
h2 = pesquisa()
h3 = pesquisa()
h4 = pesquisa()
h5 = pesquisa()

h1 = dados(genero = 'm', idade= 30, olhos= 'c', cabelo= 'p')
h2 = dados(genero = 'f', idade= 18, olhos= 'a', cabelo= 'c')
h3 = dados(genero = 'F', idade= 20, olhos= 'A', cabelo= 'L')
h4 = dados(genero = 'f', idade= 15, olhos= 'a', cabelo= 'c')
h5 = dados(genero = 'm', idade= 40, olhos= 'c', cabelo= 'p')

print('Media', media(h1,h2,h3,h4,h5))
velho = mais_velho((h1['idade'], h2['idade'], h3['idade'], h4['idade'], h5['idade']))
if velho == 0:
    print('Habitante 1 é o mais velho')
elif velho == 1:
    print('Habitante 2 é o mais velho')
elif velho == 2:
    print('Habitante 3 é o mais velho')
elif velho == 3:
    print('Habitante 4 é o mais velho')
elif velho == 4:
    print('Habitante 5 é o mais velho')

print(interesseiro(h1,h2,h3,h4,h5))
