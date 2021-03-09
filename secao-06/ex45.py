"""
45. Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa. Você deve criar 
um menu com as duas opções de conversão e com uma opção para finalizar o programa. O usuário poderá fazer 
quantas conversões desejar, sendo que o programa só será finalizado quando a opção de finalizar for escolhida.

"""

n = input('informe a velociade desejada: ')
while n.lower() != 'f':
    
    opcoes = int(input('''Digite [1] para conversão de Km/h para m/s
                       \n       [2] para conversão de m/s para Km/h 
                       \n Observação somente 1 ou 2 serão respostas aceitas\nR.= '''))
    if opcoes != 1 and opcoes != 2:
        opcoes = int(input('''Digite [1] para conversão de Km/h para m/s
                       \n       [2] para conversão de m/s para Km/h 
                       \n Observação somente 1 ou 2 serão respostas aceitas\nR.= '''))
    
    if n.isdigit() is True:
        if opcoes == 1:
            m = float(n) / 3.6
            print(f'{n}Km/h em m/s é {"%.2f" % m} ')
        else:
            opcoes == 2
            k = float(n) * 3.6
            print(f'{n}m/s em Km/h é {"%.2f" % k} ')
    else:
        print('Digite [f] para sair ou um número valido para converesão')
        n = input('informe a velociade desejada: ')
    
    n = input('Para sair digite [f] ou Informe uma velociade desejada: ')
    if n == 'f':
        break

#Resolvi fazer assim por acho mais completo 