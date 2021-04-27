"""
16. Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando vários
símbolos de igual (Ex: ========). A função recebe por parâmetro quantos sinais de igual serão
mostrados.

"""

def DesenhaLinha(quant):
    return '=' * quant

quant = int(input('Informe a qauntidade para repetir o sinal: '))
print(DesenhaLinha(quant))
