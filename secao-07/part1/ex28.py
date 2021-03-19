"""
28. Leia 10 números inteiros e armazene em um vetor v. Crie dois novos vetores vl e v2. Copie os
valores ímpares de v para v1, e os valores pares de v para v2. Note que cada um dos vetores 
v1 e v2 têm no máximo 10 elementos, mas nem todos os elementos são utilizados. No final escreva
os elementos UTILIZADOS de v1 e v2.

"""

v = []
v1 = []
v2 = []
for vetor in range(0, 10):
    num = int(input('Digite um número para o vetor: '))
    v.append(num)

for i in v:
    if i % 2 != 0:
        v1.append(i)
    else:
        i % 2 == 0
        v2.append(i)

print(v1)
print(v2)
