"""
38. Faça um programa que calcule o terno pitagorico a, b, c, para o qual a+b+c= 1000. Um terno pitagorico
é um conjunto de três números naturais, a, b, c, para a qual,

.             a² + b² = c ²
Por exemplo,

.           3² + 4² = 9 + 16 = 25 = 5²

"""

x = int(input('a + b + c = x . Digite o valor de x: '))
a = 1 
while a < x:
    b = a
    while b < x:
        c = (a ** 2 + b ** 2) ** 0.5
        if a ** 2 + b ** 2 == x:
            print(f'{a}², {b}², {c}²')
        b += 1
    a += 1
print('Fim')
