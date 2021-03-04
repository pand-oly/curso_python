"""
22. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As 
condições para aposentadoria são

• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

""" 

idade = int(input('Informe a idade do trabalhador '))
tempo = int(input('Informe o tempo de serviço '))

if idade >= 65:
    print('Na hora de aposentar meu vêio')
elif tempo >= 30:
    print('Na hora de aposentar meu vêio')
elif idade >= 60 and tempo >= 25:
    print('Na hora de aposentar meu vêio')
else:
    print('Ainda não vai trabalhar')