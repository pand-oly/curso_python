"""
17. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:

                    A = (basemaior + basemenor) * altura
                                  2                             
Lembre-se a base maior e a base menor devem ser números maiores que zero.

"""

BaseMaior = int(input('Infome o valor da base maior: '))
BaseMenor = int(input('Infome o valor da base menor: '))
altura = int(input('Informe o valor da altura: '))

a = ((BaseMaior + BaseMenor) * altura) / 2

print(a)
