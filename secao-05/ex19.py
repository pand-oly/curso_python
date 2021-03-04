"""
19. Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, 
mas não simultaneamente pelos dois.

"""
divisivel3 = False
divisivel5 = False
divisivel3e5 = False

numero = int(input('Informe um número: '))


if numero % 3 == 0 and numero % 5 == 0:
    print('Invalido: divisivel por 3 e 5 simultaneamente')
elif numero % 3 == 0:
    print('Valido: divisivel por 3')
elif numero % 5 == 0:
    print('Valido: divisivel por 5')
else:
    print('Invalido: não divisivel por 3 ou 5')
