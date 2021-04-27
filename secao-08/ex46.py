"""
46. Crie um programa contendo as seguintes funções que recebem um vetor V números reais
como parâmetro:

• Impressão normal do vetor.
• Impressão inversa.
• Função que retorna a média aritmética dos elementos do vetor.

"""

v = [1.1, 1.2, 1.3, 1.4, 1.5, 1.9]

def vetor(v):
    invero = v.copy()[::-1]
    media = sum(v) / len(v)

    return f'• {v} \n• {invero} \n• {"%.2f" % media}'

print(vetor(v))
