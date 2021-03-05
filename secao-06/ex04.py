"""
4. Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000
em 1000, imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).

"""
mil = 0
numb = int(input('Digite um número inteiro: '))
while numb <= 100_000 or mil <= 100_000:
    if numb <= 100_000 or mil <= 100_000:
        if mil <= numb:        #caso numero for negativo
            print(mil)
            if numb < 100_000: # para que valor não ultrapasse cem mil
                print(numb)
        else:
            if numb < 100_000:
                print(numb)
            print(mil)
    
    numb = numb + 1000
    mil = mil + 1000