"""
14. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação 
Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado
(média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações 
necessárias.

"""

nota1 = float(input('Informe a nota do trabalho de laboratório: '))
nota2 = float(input('Informe a nota da avaliação semestral: ')) 
nota3 = float(input('Informe a nota do exame final: '))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
print(media)
if media <= 2.9:
    print('Reprovado')
elif media >= 3 and media <= 4.9:
    print('Você esta de recuperação')
else:
    print('Aprovado')
