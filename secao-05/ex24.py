"""
24. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente 
de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor 
e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em 
que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.

"""

valor = int(input('Informe o valor do produto: '))
uf = input('Informe a UF do estado no qual deseja o envio: ')

if uf.upper() == 'MG':
    percentual = valor * 0.07
    ValorTotal = valor + percentual
    print(f'Preço: {ValorTotal}')
elif uf.upper() == 'SP':
    percentual = valor * 0.12
    ValorTotal = valor + percentual
    print(f'Preço: {ValorTotal}')
elif uf.upper() == 'RJ':
    percentual = valor * 0.15
    ValorTotal = valor + percentual
    print(f'Preço: {ValorTotal}')
elif uf.upper() == 'MS':
    percentual = valor * 0.08
    ValorTotal = valor + percentual
    print(f'Preço: {ValorTotal}')
else:
    print('Não a entrega neste estado')
