"""
20. Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o 
número de dados lidos e número de valores pares. O processo termina quando for digitado o número 1000.

"""

pergunta = 0
while pergunta != 1000:
    q = int(input('Quantas vezes fazer a pergunta: '))
    for i in range(1, q + 1):
        numero = int(input('Digite um numero inteiro e positivo: '))
        if numero >= 0:
            if numero % 2 == 0:
                print('Par')
            else:
                print('Não par')
        else:
            numero = int(input('Digite um numero inteiro e positivo: '))
    
    pergunta = int(input('continuar? Para fechar o programa digite 1000  '))
