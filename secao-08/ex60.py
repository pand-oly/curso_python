"""
60. Escreva uma função que retorne a primeira posição de uma sub-string dentro de uma
string. Caso a sub-string não seja encontrada, a função deve retornar -1.

"""

texto = "Um pequeno  texto  para testar o meu programa"


def position(texto):
    return texto.find('oja')

print(position(texto))
