from random import *
#
#cartela = [[], [], [8]]
#var = False
#for l in range(0, 3):
#    while len(cartela[l]) < 3:
#        num = randint(1, 9)
#        for i in range(0, 3):
#            while num in cartela[i]:
#                num = randint(1, 9)
#        cartela[l].append(num)
#
#print(cartela)
"""
cont = 0
for l in range(0, 3):
    for c in range(0, 3):
        v = cartela[c][l]
        verifc = (cartela[l].count(v))
        cont += verifc
        break
    

print('c', cont)
"""
"""
#st = set({1, 2, 3, 4, 5, 6, 7, 5, 8, 9})
st = set({})
for i in range(0, 9):
    num = (input('Informe um número: '))
    set.add(num)
    print(st)
    """

st = set({})
while len(st) < 9:
    num = int(randint(0, 9))
    #num = int(input('Informe um número: '))
    st.add(num)
print(st)

cartela = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = 0
n = 0
l = 0
c = 0
while cont < 8:
    for valor in st:
        if cont == n:
            n += 1
            break
        cont += 1
        print(cont)
        print(c)
        if l < 3:
            c += 1
        cartela[c][l] = valor
        l += 1
        print(l)
print(cartela)