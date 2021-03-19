"""
31. Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união entre
os 2 vetores anteriores, ou seja, que contém os números dos dois vetores. Não deve conter números
repetidos.

"""

vetor1 = ({1, 3, 4, 56, 67, 34, 2, 64, 8, 376, 5})
vetor2 = ({3, 4, 5, 7, 2, 67, 6, 54, 34, 48, 76, 8})

novo = vetor1.copy()
novo.update(vetor2.copy())

print(novo)