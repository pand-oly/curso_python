"""
17. Leia um vetor de 10 posições e atribua valor o para todos os elementos que possuírem
valores negativos.

"""

vetor = []
for v in range(0, 10):
    num = int(input('Informe um número: '))
    vetor.append(num)

print(vetor)
quant = (len(vetor))
p = 0
while p < quant:
    if vetor[p] < 0:
        vetor[p] = int(input('Informe novo valor positivo para esta posição: '))
    
    p += 1

print(vetor)