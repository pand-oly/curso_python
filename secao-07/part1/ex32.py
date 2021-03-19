"""
32. Leia dois vetores de inteiros X e Y, cada um com 5 elementos (assuma que o usuário não
informa elementos repetidos). Calcule e mostre os vetores resultantes em cada caso abaixo:

• Soma entre X e Y: soma de cada elemento de X com o elemento da mesma posição em Y.
• Produto entre X e Y: multiplicação de cada elemento de X como elemento da mesma posição em Y.
• Diferença entre X e Y: todos os elementos de X que não existam em Y.
• Interseção entre X e Y: apenas os elementos que aparecem nos dois vetores.
• União entre X e Y: todos os elementos de X, e todos os elementos de X que não estão em X.

"""

vetor1 = []
vetor2 = []
while len(vetor1) < 5:
    num = int(input('Informe um número para o primeiro vetor: '))
    if num in vetor1:
        num = int(input('Repetiu informe novamente um número: '))
    else:
        vetor1.append(num)

while len(vetor2) < 5:
    num = int(input('Informe um número para o segundo vetor: '))
    if num in vetor2:
        num = int(input('Repetiu informe novamente um número: '))
    else:
        vetor2.append(num)

# 1° e 2° topico 
soma = []
mult = []
for i in range(0, len(vetor1)):
    s = vetor1[i] + vetor2[i]
    soma.append(s)
    m = vetor1[i] * vetor2[i]
    mult.append(m)

print(soma)
print(mult)

# 3° topico
vetor1 = set(vetor1)
dif = vetor1.difference(vetor2)
print(dif)

# 4° topico
inter = vetor1.intersection(vetor2)
print(inter)

# 5° topico
union = vetor1.union(vetor2)
print(union)
