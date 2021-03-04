"""Só algumas anotações sobre input e printe pra não esquecer

input() -> Todo dado recebido via input é do tipo string
"""
nome = input('Qual seu nome?\n')
# nome = input() #input -> Entrada

# exemplo de print antigo 2.x
# print('Seja bem vindo(a) %s' % nome)

# exemplo de print antigo 3.x
# print('Seja bem vindo(a) {0}'.formate{nome})

# exemplo de print mais atual 3.7
print(f'Seja bem vindo {nome}')

idade = int(input('Qual sua idade?\n'))
print(f'Olha você tem {idade} anos')

print(f'\'{nome} tem {idade} anos\'')
