"""
63. Crie uma função que compara duas strings e que retorna se elas são iguais ou diferentes. 

"""


def compare(str1, str2):
    if str1 == str2:
        return 'Iguais'
    return 'Diferentes'

str1 = 'assim'
str2 = 'assado'
print(compare(str1, str2))