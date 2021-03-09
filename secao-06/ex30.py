"""
30. Faça programas para calcular as seguintes sequências:

1 + 2 + 3 + 4 + 5 + ...+n
1 - 2 + 3 - 4  + 5 + ... + (2n-1)
1 + 3 +5 + 7 + ... + (2n-1)

"""

n = int(input('Informe o valor de N: '))
q = int(input('Informe valor final contagem: '))
a = 0
b = 0
c = 0
for i in range(1, q + 1):
    a = a + i
    
    if i % 2 == 0:
        b = b - i
    else:
        b = b + i
        c = c + i

a = a + n
b = b + (2 * n - 1)
c = c + (2 * n - 1)

print(a)
print(b)
print(c)
