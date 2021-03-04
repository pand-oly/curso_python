"""
40. O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos 
impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. 
Leia o custo de fábrica e escreva o custo ao consumidor.
________________________________________________________________
|____CUSTO DE FÁBRICA______|_% DO DISTRIBUIDOR_|_% DOS IMPOSTOS_|
| até R$12.000,00 entre    |        5          |     isento     |
| R$ 12.000,00 e 25.000,00 |        10         |       15       |  
| acima de R$25.000,00     |        15         |       20       | 
-----------------------------------------------------------------

"""

custo = float(input('Digite o custo de fabrica do carro: '))

if custo <= 12_000:
    distribuidor = 0.05
    imposto = 'insento'
elif custo <= 25_000:
    distribuidor = 0.1
    imposto = 0.15
elif custo > 25_000:
    distribuidor = 0.15
    imposto = 0.2

if imposto == 'insento':
    imposto = 0

custo = custo + (custo * distribuidor) + (custo * imposto)

print(f'Custo ao cosumidor R${"%.2f" % custo}')