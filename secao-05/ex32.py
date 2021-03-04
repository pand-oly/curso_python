"""
32. Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente será 
calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:
____________________________________
| Especificação   | Código | Preço |
|-----------------|--------|-------|
| Cachorro Quente |  100   | 1.20  |
| Bauru Simples   |  101   | 1.30  |
| Bauru com Ovo   |  102   | 1.50  |
| Hamburguer      |  103   | 1.20  |
| Cheeseburguer   |  104   | 1.70  |
| Suco            |  105   | 2.20  |
| Refrigerante    |  106   | 1.00  |
------------------------------------
"""
ValorTotal = 0
codico = int(input('Digite o códico do pedido: '))

while codico != 0:
    quantidade = int(input('Informe a quantidadedeste pedido: '))
    if codico == 100:
        pedido = 1.2
    if codico == 101:
        pedido = 1.3
    if codico == 102:
        pedido = 1.5
    if codico == 103:
        pedido = 1.2
    if codico == 104:
        pedido = 1.7
    if codico == 105:
        pedido = 2.2
    if codico == 106:
        pedido = 1.0   
    valor = pedido * quantidade
    ValorTotal = ValorTotal + valor
    codico = int(input('Deseja pedir algo  mais? Digite o códico do pedido: '))

print(f'Total do seu pedido é {ValorTotal}')