with open('file.txt', 'r') as fil:
    cont = len(fil.readlines())
    fil.seek(0)
    total = 0
    for i in range(cont):
        line = fil.readline().split(' ')
        nome = line[0]
        preco = line[1]
        total += float(preco)

print(total)
