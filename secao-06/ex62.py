"""
62. Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro, cinco, então há
2 +4 +4 +6 +5 = 22 letras usadas no total. Faça um programa que conte quantas letras seriam 
utilizadas se todos os números de 1 a 1000 (mil) fossem escritos em palavras. OBS: Não conte
espaços ou hifens.

"""

num = 1
l = ''
while num <= 1000:
    cont = 0
    for x in str(num):
        cont += 1         #valor do contador tem relação com as casas

    n = num
    while n > 0:
        if cont == 1:
            if n == 1:
                l += ' um '
                n -= 1
            elif n == 2:
                l += ' dois '
                n -= 2
            elif n == 3:
                l += ' tres '
                n -= 3
            elif n == 4:
                l += ' quatro '
                n -= 4
            elif n == 5:
                l += ' cinco '
                n -= 5
            elif n == 6:
                l += ' seis '
                n -= 6
            elif n == 7:
                l += ' sete '
                n -= 7
            elif n == 8:
                l += ' oito '
                n -= 8
            elif n == 9:
                l += ' nove '
                n -= 9
        elif cont == 2:
            if n == 10:
                l += 'dez '
                n -= 10
            elif n == 11:
                l += ' onze '
                n -= 11
            elif n == 12:
                l += ' doze '
                n -= 12
            elif n == 13:
                l += ' treze '
                n -= 13
            elif n == 14:
                l += ' quatorze '
                n -= 14
            elif n == 15:
                l += ' quinze '
                n -= 15
            elif n == 16:
                l += ' dezesseis '
                n -= 16
            elif n == 17:
                l += ' dezessete '
                n -= 17
            elif n == 18:
                l += ' dezoito '
                n -= 18
            elif n == 19:
                l += ' dezenove '
                n -= 19
            elif n == 20:
                l += ' vinte '
                n -= 20
            elif n > 20 and n < 30:
                l += ' vinte e '
                n -= 20
                cont -= 1    #deve tirar um numero do contador para que não rode infino
            elif n == 30:
                l += ' trinta '
                n -= 30
            elif n > 30 and n < 40:
                l += ' trinta e '
                n -= 30
                cont -= 1
            elif n == 40:
                l += ' quarenta '
                n -= 40
            elif n > 40 and n < 50:
                l += ' quarenta e '
                n -= 40
                cont -= 1
            elif n == 50:
                l += ' cinquenta '
                n -= 50
            elif n > 50 and n < 60:
                l += ' cinquenta e '
                n -= 50
                cont -= 1
            elif n == 60:
                l += ' sessenta '
                n -= 60
            elif n > 60 and n < 70:
                l += ' sessenta e '
                n -= 60
                cont -= 1
            elif n == 70:
                l += ' setenta '
                n -= 70
            elif n > 70 and n < 80:
                l += ' setenta e '
                n -= 70
                cont -= 1
            elif n == 80:
                l += ' oitenta '
                n -= 80
            elif n > 80 and n < 90:
                l += ' oitenta e '
                n -= 80
                cont -= 1
            elif n == 90:
                l += ' noventa '
                n -= 90
            elif n > 90 and n < 100:
                l += ' noventa e '
                n -= 90
                cont -= 1
            cont = 1
        elif cont == 3:
            if n == 100:
                l += ' cem '
                n -= 100
                cont = 2
            elif n >= 100 and n < 200:
                l += ' cento e '
                n -= 100
                cont = 2
            if n == 200:
                l += ' duzentos '
                n -= 200
                cont = 2
            elif n >= 200 and n < 300:
                l += ' duzentos e '
                n -= 200
                cont = 2
            if n == 300:
                l += ' trezentos '
                n -= 300
                cont -= 1
            elif n >= 300 and n < 400:
                l += ' trezentos e '
                n -= 300
                cont = 2
            if n == 400:
                l += ' quatrocentos '
                n -= 400
                cont = 2
            elif n >= 400 and n < 500:
                l += ' quatrocentos e '
                n -= 400
                cont = 2
            if n == 500:
                l += ' quinhentos '
                n -= 500
                cont -= 1
            elif n >= 500 and n < 600:
                l += ' quinhentos e '
                n -= 500
                cont = 2
            if n == 600:
                l += ' seissentos '
                n -= 600
                cont = 2
            elif n >= 600 and n < 700:
                l += ' seissentos e '
                n -= 600
                cont = 2
            if n == 700:
                l += ' setessentos '
                n -= 700
                cont -= 1
            elif n >= 700 and n < 800:
                l += ' setessentos e '
                n -= 700
                cont = 2
            if n == 800:
                l += ' oitossentos '
                n -= 800
                cont = 2
            elif n >= 800 and n < 900:
                l += ' oitossentos e '
                n -= 800
                cont = 2
            if n == 900:
                l += ' novessentos '
                n -= 900
                cont = 2
            elif n >= 900 and n < 1000:
                l += ' novessentos e '
                n -= 900
                cont = 2
        elif cont == 4:
            if n == 1000:
                l += ' mil '
                n -= 1000
                cont = 3
            elif n >= 1000 and n < 2000:
                l += ' mil e '
                n -= 1000
                cont = 3

    num += 1

print(l)
s = l.split()
space = ''.join(s)
c = 0

for i in str(space):
    c += 1

print(f'De 1 ate 1000 tem {c} letras se duvida conta ai.')