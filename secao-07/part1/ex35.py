"""
35. Faça um programa que leia dois números a e b (positivos menores que 10000) e:

• Crie um vetor onde cada posição é um algarismo do número. A primeira posição é
o algarismo menos significativo;
• Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores construídos
anteriormente.

Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia 10 do resultado e
some 1 à proxima posição.

"""
a = int(input('Informe o número de A: '))
b = int(input('Informe o número de B: '))

vetorA = []
while a > 0:
    n = a % 10
    vetorA.append(n)
    a = int(a / 10)
print(vetorA)

vetorB = []
while b > 0:
    n = b % 10
    vetorB.append(n)
    b = int(b / 10)
print(vetorB)

vetor3 = []
extra = 0
for i in range(len(vetorA)):
    soma = extra + vetorA[i] + vetorB[i]
    extra = 0
    if soma >= 10:
        soma -= 10
        extra = 1
    vetor3.append(soma)

if extra > 0:
    vetor3.append(extra)

print(vetor3)


# dois metodos para lembrar
'''
a = 356
b = str(a)
vetor = []
soma = 0
while a > 0:
    n = a % 10
    vetor.append(n)
    a = int(a / 10)
print(vetor[::-1])


vetor2 = []
for i in range(len(b)):
    v = int(b[i])
    vetor2.append(v)
print(vetor2)

'''