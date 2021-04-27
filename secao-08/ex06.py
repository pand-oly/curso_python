"""
6. Faça uma função que receba 3 números inteiros como parâmetro, representando horas,
minutos e segundos, e os converta em segundos.

"""

h = '02:40:20'
horas, minutos, segundos = h.split(':')
horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)

def calculo(horas, minutos, segundos):
    TotalSegundos = segundos
    TotalSegundos += horas * 3600
    TotalSegundos += minutos * 60
    return TotalSegundos

print(calculo(horas, minutos, segundos))
