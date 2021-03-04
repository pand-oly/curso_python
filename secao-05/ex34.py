"""
34. Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.
__________________________________________________________________________
| NOTA         | CONCEITO (ATÉ 20 FALTAS) | CONCEITO (MAIS DE 20 FALTAS) |
| 9.0 até 10.0 |           A              |              B               |
| 7.5 até 8.9  |           B              |              C               |
| 5.0 até 7.4  |           C              |              D               |
| 4.0 até 4.9  |           D              |              E               |
| 0.0 até 3.9  |           E              |              E               |
--------------------------------------------------------------------------

"""

nota = float(input('Informe a nota: '))
faltas = int(input('Digite o número de faltas: '))

if faltas <= 20:
    if nota >= 9.0 and nota <= 10.0:
        print('Nota A')
    elif nota >= 7.5 and nota <= 8.9:
        print('Nota B')
    elif nota >= 5.0 and nota <= 7.4:
        print('Nota C')
    elif nota >= 4.0 and nota <= 4.9:
        print('Nota D')
    elif nota >= 0.0 and nota <= 3.9:
        print('Nota E')
    else:
        print('Erro Nota')
elif faltas > 20:
    if nota >= 9.0 and nota <= 10.0:
        print('Nota B')
    elif nota >= 7.5 and nota <= 8.9:
        print('Nota C')
    elif nota >= 5.0 and nota <= 7.4:
        print('Nota D')
    elif nota >= 4.0 and nota <= 4.9:
        print('Nota E')
    elif nota >= 0.0 and nota <= 3.9:
        print('Nota E')
    else:
        print('Erro Nota')