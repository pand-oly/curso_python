"""
15. Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos
repetidos.

"""

vetor = []
for i in range(0, 10):
    num = int(input('Informe um número: '))
    vetor.append(num)

print(vetor)

                # fiz desta forma casa a lista ja esteja pronta e não digitada pelo usuario
for i in vetor:
    if vetor.count(i) > 1:
        posicion = (vetor.index(i)) # Usei posicion para indentificar primeira posção do numero
        cont = vetor.count(i)          # que se repete para que este não seja removido
        for rep in range(1, cont):      # Este for é para remover os numeros repetidos 
            posicion1 = vetor.index(i, posicion + 1)  # posicion1 é onde esta os numeros repetidos
            vetor.pop(posicion1)
        
print(vetor)