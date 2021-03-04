"""
13. Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos. 

"""

prova1 = float(input('Informa a nota da primeira prova: '))
prova2 = float(input('Informa a nota da segunda prova: '))
prova3 = float(input('Informa a nota da terceira prova: '))

media = (prova1 + prova2 + prova3 * 2) / 4

if media > 60:
    print(f'Sua media foi: {media}, e você foi: Aprovado')
else:
    print(f'Sua media foi: {media}, e você foi: Reprovado')
