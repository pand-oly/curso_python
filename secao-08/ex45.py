"""
45. Faça uma função que calcule o desvio padrão de um vetor v contendo n números

Desvio Padrão:

onde me a media do vetor.

"""

vetor = []
for v in range(0, 10):
    num = int(input('Digite um número para o vetor: '))
    vetor.append(num)


media = sum(vetor) / len(vetor)

def mv(media):
    MediaVetor = []
    for i in vetor:
        dp = i - media
        MediaVetor.append(dp)
    return MediaVetor
    
MediaVetor = mv(media)


def quadrado(MediaVetor):
    SquareVector = []
    for m in MediaVetor:
        square = m ** 2
        SquareVector.append(square)
    
    return SquareVector


SquareVector = quadrado(MediaVetor)

def dp(SquareVector):
    MediaDp = sum(SquareVector) / len(vetor)
    DesvioPadrao = MediaDp ** 0.5

    return DesvioPadrao

print(dp(SquareVector))
