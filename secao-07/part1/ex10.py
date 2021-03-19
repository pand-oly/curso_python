"""
10. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
e imprima a média geral.

"""

nota = []
for i in range(0, 15):
    i = float(input('Informe a nota do aluno: '))
    nota.append(i)

soma = sum(nota)
print('A media da nota dos alunos é ', soma / 15 )