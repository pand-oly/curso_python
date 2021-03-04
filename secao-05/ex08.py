"""
8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina.

"""

nota1 = float(input('Informe a nota da primeira prova: '))
nota2 = float(input('Informe a nota da segunda prova: '))

if (nota1 > 0.0, nota1 < 10.0, nota2 > 0.0, nota2 < 10.0):
    print((nota1 + nota2) / 2)
