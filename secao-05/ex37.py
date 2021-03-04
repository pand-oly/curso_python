"""
37. As tarifas de certo parque de estacionamento são as seguintes:

• 1° e 2° hora - R$ 1,00 cada
• 3° e 4° hora - R$ 1,40 cada
• 5° hora e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 
61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos 
de chegada ao parque e partida deste são apresentados na forma de pares de inteiros, representando horas e 
minutos. Por exemplo, o par 12 50 representará "dez para a uma da tarde". Pretende-se criar um programa que,
lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento.
Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora
de chegada for superior à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu
no dia seguinte ao da chegada.

"""
from datetime import datetime, timedelta, time

preco1 = 1.0
preco2 = 1.4
preco3 = 2.0

# Entrada de dados
chegada = input('Digite seus dados de chegada: "HH:MM" ')
saida = input('Informe seus dados de saida: "HH:MM" ')
dia_entrada = input("Coloque o dia de entrada no formato dd/mm/yyyy")
dia_saida = input("Coloque o dia de saida no formato dd/mm/yyyy")

# Calculo de tempo
dia_e,mes_e,ano_e = dia_entrada.split("/") # Separando o dia dos meses e ano
dia_e = int(dia_e)
dia_s,mes_s,ano_s = dia_saida.split("/")  # Separando o dia dos meses e ano
dia_s = int(dia_s)
fmt = '%H:%M'
tdelta = datetime.strptime(saida, fmt) - datetime.strptime(chegada, fmt)
if tdelta.days < 0:
    tdelta = timedelta(days=0, seconds=tdelta.seconds,
        microseconds=tdelta.microseconds)

seconds = tdelta.total_seconds()
minutos = seconds // 60

if dia_entrada == dia_saida: 
    if minutos <= 60:
        cobrar = 1 * preco1
    elif minutos > 60 and minutos <= 120:
        cobrar = 2 * preco1      
    elif minutos > 120 and minutos <= 180:
        cobrar = 3 * preco2
    elif minutos > 180 and minutos <= 240:
        cobrar = 4 * preco2
    elif minutos > 240:
        horas = seconds // 3600
        RestoHoras = seconds % 3600
        minut = RestoHoras // 60
        if minut > 0:
            h = horas + 1
            cobrar = preco3 * h
        else:
            cobrar = preco3 * horas
elif dia_entrada != dia_saida:
    tdelta + 24
    horas = seconds // 3600
    RestoHoras = seconds % 3600
    minut = RestoHoras // 60
    if minut > 0:
        h = horas + 1
        cobrar = preco3 * (h + 24)
    else:
        cobrar = preco3 * (horas + 24)

print(f'Entrada as {chegada}; E saida as {saida};O tempo que ficou é {tdelta} Valor a se cobrar R${"%.2f" % cobrar}')