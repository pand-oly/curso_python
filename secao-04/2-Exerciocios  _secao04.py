""" 1. Faça um programa que leia um número inteiro e o imprima. """
# 1
numero = 1
print(numero)

" 2. Faça um programa que leia um número real e o imprima."
# 2
NumeroReal = 2
print(NumeroReal)

" 3. Peça ao usuário para digitar três valores inteiros e imprima a soma deles."
# 3
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))
soma = (numero1 + numero2 + numero3)
print(soma)

" 4. Leia um número real e imprima o quadrado desse número"
# 4
numero4 = 2.0
print(numero4 ** 2)

" 5. Leia um número real e imprima a quinta parte deste numero "
# 5
numero5 = 25
print(int(numero5 / 5))

""" 6. Leia uma temperatura em graus Celsius e apresente-a convertida em gruas Fahrenheit. A fórmula de conversão é:  
F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em gruas Celsius"""
# 6
c = -14.4444
f = c * (9.0 / 5.0) + 32.0
print("%.1f" % f)

""" 7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em gruas Celsius. A fórmula de conversão é:  
C = 5.0*(f-32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit"""
# 7
f = 44.6
c = 5.0 * (f - 32.0) / 9.0
print("%.1f" % c)

""" 8. Leia uma temperatura em graus Kelvin e apresente-a convertida em gruas Celsius. A fórmula de conversão é:  
C = k - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin"""
k = 281.15
c = float(k - 273.15)
print(c)

""" 9. Leia uma temperatura em graus Celsius e apresente-a convertida em gruas Kelvin. A fórmula de conversão é:  
K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin"""
# 9
c = -264.15
k = c + 273.15
print(k)

""" 10. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M= K /3.6, sendo K a velocidade em
km/h e M em m/s."""
k = 36
m = k / 3.6
print(m)

""" 11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilómetros por hora). A fórmula de conversão é: K = M*3,6, sendo K a velocidade
em km/h e M em rn/s."""
m = 3.06
k = m * 3.6
print(k)

""" 12. Leia uma distância em milhas e apresente-a convertida em quilómetros. A fórmula de
conversão é: K = 1,61*M, sendo K a distância em quilómetros e M em milhas."""
m = 7.46
k = 1.61 * m
print(k)

""" 13. Leia uma distância em quilómetros e apresente-a convertida em milhas. A fórmula de
conversão é: M = k/1.61, sendo K a distância em quilômetros e M em milhas."""
k = 20.92
m = k / 1.61
print(m)

""" 14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R = G * þ/180, sendo G o ângulo em graus e R em radianos e 3.14. # {þ = pi} """
import math

p = math.pi
g = float(input('Angulo para conversão'))
r = float(g * p / 180)
print("%.4f" % r)

""" 15. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é: G = R*180/þ, sendo G o ângulo em graus, R em radianos e þ em pi."""
import math

r = 6.28
g = r * 180 / math.pi
print("%.4f" % g)

""" 16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2,54, sendo C o comprimento em centímetros e P o
comprimento em polegadas."""
# 16
p = 6.3
c = p * 2.54
print("%.4f" % c)

""" 17. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C/2,54,sendo C o comprimento em centímetros e P o comprimento em polegadas."""
# 17
c = 43.18
p = c / 2.54
print("%.4f" % p)

""" 18. Leia um valor de volume em metros cúbicos M³ e apresente-o convertido em litros. A
fórmula de conversão é: L = 1000*M, sendo L o volume em litros e M o volume em
metros cúbicos."""
m = 0.018
l = 1000 * m
print(l)

""" 19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³ 
fórmula de conversão é: M = L/1000 sendo L o volume em litros e M c volume em metros cúbicos."""
l = 19000
m = l / 1000
print(m)

""" 20. Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula
de conversão é: L = k/0.45 sendo K a massa em quilogramas e L a massa em libras."""
k = 9
l = k / 0.45
print(l)

""" 21. Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula
de conversão é: K = L*0,45, sendo K a massa em quilogramas e L a massa em libras."""
l = 19.84
k = l * 0.45
print(k)

""" 22. Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = O,91 * J, sendo J o comprimento em jardas e M o comprimento
em metros."""
j = 24.01
m = 0.91 * j
print(m)

""" 23. Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula
de conversão é: J = m/0.91, sendo J o comprimento em jardas e M o comprimento em metros."""
m = 21
j = m / 0.91
print(j)

""" 24. Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A
fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e a área em acres."""
m = 97124.6
a = m * 0.000247
print(a)

""" 25. Leia um valor de área em acres e apresente-o convertido em metros quadrados. A
fórmula de conversão é: M = A * 4048,58, sendo M a área em metros quadrados e a área em acres."""
a = 6
m = a * 4048.58
print(m)

""" 26. Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H = M * 0,0001, sendo M a área em metros quadrados e H a área em hectares."""
m = 260000
h = m * 0.0001
print(h)

""" 27. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares."""
h = 0.0027
m = h * 10000
print(m)

""" 28. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos
três valores lidos."""
n28_1 = 2
n28_2 = 2
n28_3 = 2
soma = (n28_1 ** 2) + (n28_2 ** 2) + (n28_3 ** 2)
print(soma)

""" 29. Leia quatro notas, calcule a média aritmética e imprima o resultado. """
nota1 = 9.0
nota2 = 9.9
nota3 = 8.5
nota4 = 7.9
Medida_aritmetica = (nota1+nota2+nota3+nota4)/4
print(Medida_aritmetica)

""" 30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente
em dólares."""
# 30
real = int(input('Digite o valor que deseja converter:\n'))
cotacao = 5.37
print(real*cotacao)


""" 31. Leia um número inteiro e imprima o seu antecessor e o seu sucessor."""
numero31 = 31
print(f'{numero31-1}, {numero31+1}')

""" 32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de 
seu dobro."""
numero32 = 32
antecessor = numero32 * 3 + 1
sucessor = numero32 * 2 - 1
print(antecessor + sucessor)

""" 33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área."""
b = 33
a = 33
print(b * a)

""" 34. Leia o valor do raio de um círculo e calcule e imprima a área dc círculo correspondente.
A área do círculo é þ*raio², considere þ = 3,141392."""
pi = 3.141392
r = 3
a = pi * r ** 2
print("%.2f" % a)

""" 35. Sejam æ, e ß os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
HIPOTENUSA = √a²+b². Faça um programa que receba os valores de a e b e calcule o valor da 
hipotenusa através da equação. Imprima o resultado dessa operação."""
a = 10
b = 5
h = (a ** 2 + b ** 2) ** 0.5
print("%.2f" % h)

""" 36. Leia a altura e o raio de um cilindro circular e imprima o volume dc cilindro. O volume de um 
cilindro circular é calculado por meio da seguinte fórmula: V = þ * raio² * altura, onde þ = 3.141392."""
pi = 3.141392
altura = 1
raio = 2
volume = pi * raio ** 2 * altura
print(volume)

""" 37. Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%."""
valor = 1000
desconto = valor * 0.12
print(desconto)

""" 38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%."""
salario = 1000
aumento = salario + (salario * 0.25)
print(f'Como seu salario era {salario}, você recebeu um aumento de 25% agora seu salario atualizado é {aumento}')

""" 39. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
 * O primeiro ganhador receberá 46%;
 * O segundo receberá 32%;
 * O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores"""
importancia = 780_000.00
primeiroG = importancia * 0.46
segundoG = importancia * 0.32
terceiroG = importancia - primeiroG - segundoG
print(f'''O primeiro ganhador leva {primeiroG};
O segundo ganhador ganha {segundoG}
E o prêmio do terceiro foi {terceiroG}''')

""" 40. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda."""
diaria = 30.00
DiasTrabalhados = int(input('Digite aqui quantos dias você trabalhou:\n'))
recibo = (diaria * DiasTrabalhados) * 0.92
print(f'O valor liquido do seu recibo é {recibo}R$')

""" 41. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado."""
HoraDeTrabalho = 50.00
HorasTrabalhadas = 6
recibo = HoraDeTrabalho * HorasTrabalhadas
adicional = recibo * 0.1
print(f'Seu pagamento é de {recibo + adicional}')

""" 42 Receba o salário base de um funcionário. Calcule e imprima o salário a receber, sabendo-
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base."""
# 42
salario = int(input('Dgite aqui seu salario:\n'))
gratificacao = salario * 0.05
imposto = salario * 0.07
print(f'O valor liquido do seu salario é {salario + gratificacao - imposto}')

""" 43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
• o total a pagar com desconto de 10%;
• o valor de cada parcela, no parcelamento de 3x sem juros;
• a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com des-
conto)
• a comissão do vendedor no caso da venda ser parcelada (5% sobre o valor total)"""
# 43
valor = int(input('Digite um o valor aqui:\n'))
desconto = valor * 0.1
parcela = valor / 3
descontoRes = valor - desconto

print(f' - A vista fica por {descontoRes}.')
print(f' - Parcelas de 3X sem juros são de {"%.2f" % parcela}')
print(f' - A comissao do vendedor do valor a vista é {descontoRes * 0.05}')
print(f' - Caso seja parcelado a comissão sera de {valor * 0.05}')

""" 44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo."""
# 44
degrau = 0.5
escada = 5
print(f'O numero de degraus é {int(escada / degrau)}')

""" 45. Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
ASCII para resolver o problema."""
# 45
maiuscuola = 'ASDFGHHJ'
minuscula = maiuscuola.lower()
print(minuscula)

""" 46. Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo.
NúmeroLido = 123
NúmeroGerado = 321."""
numero47 = '123'[::-1]
print(int(numero47))

""" 47. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha."""
numero48 = '1234'
print(f'{numero48[0]}\n{numero48[1]}\n{numero48[2]}\n{numero48[3]}')

""" 48. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos."""
valor = 20_000
horas = valor // 3600
resto = valor % 3600
minutos = resto // 60
segundos = resto % 60

print(f'Horas:Minutos:Segundos \n{horas}:{minutos}:{segundos}')

""" 49. Faça um programa para leia o horário (hora, minuto e segundo) de inicio e aduração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do termino da mesma."""
# 49
hora = int(input('Digite o horário de inicio da experiência(horas):'))
minuto = int(input('(minutos):'))
segundo = int(input('(segundos):'))
duracao = int(input('Digite a duração do experimento(segundos):'))

hor = duracao // 3600
resto = duracao % 3600
min = resto // 60
seg = resto % 60

horas_f = hora + hor
minutos_f = minuto + min
segundos_f = segundo + seg

if minutos_f >= 60:
    minutos_f -= 60
    horas_f += 1
else:
    var = ()

if segundos_f >= 60:
    segundos_f -= 60
    minutos_f += 1
else:
    var = ()

print(f'{horas_f:02}:{minutos_f:02}:{segundos_f:02}')

""" 50. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual."""
# 50
idade = int(input('Digite sua idade: '))
ano = int(input('Digite o ano: '))
print(f'A sua data de nascimento é {ano - idade}')

""" 51. Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua
distância da origem (O,O)."""
x1 = 3
y1 = 5
x2 = 4
y2 = 7

x = int((x1 ** 2 + x2 ** 2) ** 0.5)
y = int((y1 ** 2 + y2 ** 2) ** 0.5)
print(f'{x},{y}')

""" 52. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido 
proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prémio, e imprima quanto cada um
ganharia do prêmio com base no valor investido."""
# 52
premio = int(input('Digite o valor do premio?\n'))
aposta1 = float(input('Quanto você apostou?\n'))
aposta2 = float(input('Quanto você apostou?\n'))
aposta3 = float(input('Quanto você apostou?\n'))

ValorTotalApost = aposta1 + aposta2 + aposta3
percentual1 = (aposta1 / ValorTotalApost) * 100/100
percentual2 = (aposta2 / ValorTotalApost) * 1.0             #100/100 é a mesma coisa 1.0 é resultado de 100/100
percentual3 = (aposta3 / ValorTotalApost) * 1.0

ganhador1 = premio * percentual1
ganhador2 = premio * percentual2
ganhador3 = premio * percentual3

print(f'''O primeiro jogador apostou {aposta1}, ganha o valor de {"%.2f" % ganhador1}
O segundo jogador apostou {aposta2}, vai ganha {"%.2f" % ganhador2}
E o terceiro jogador que a aposta de {aposta3}, recebe o valor de {"%.2f" % ganhador3}''')

""" 53. Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno
com tela."""
c = 100
l = 50
p = 5.50
t = c * l
print(f'{t * p} R$')
