"""
26. Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números,
onde m é a media do vetor.

Desvio Padrão =
(vi) - m)2
2=1

£

"""

vetor = []
for v in range(0, 10):
    num = int(input('Digite um número para o vetor: '))
    vetor.append(num)

#print(vetor)

media = sum(vetor) / len(vetor)
#print(media)

MediaVetor = []
for i in vetor:
    dp = i - media
    MediaVetor.append(dp)

#print(MediaVetor)

SquareVector = []
for m in MediaVetor:
    square = m ** 2
    SquareVector.append(square)

#print(SquareVector)

MediaDp = sum(SquareVector) / len(vetor)
#print(MediaDp)

DesvioPadrao = MediaDp ** 0.5
print('dp = ', DesvioPadrao)
