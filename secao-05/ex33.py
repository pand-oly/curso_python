"""
33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o 
preço novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).
_______________________________________________
| PRECO ANTIGO         | PERCENTUAL DE AUMENTO |
| até R$ 50            |       5%              |
| entre R$ 50 e R$ 100 |      10%              |
| acima de R$ 100      |      15%              |
------------------------------------------------
________________________________________________
|         PREÇO NOVO               | MENSAGEM   |
|até R$ 80                         | Barato     |
|entre R$ 80 e R$ 120 (inclusive)  | Normal     |
|entre R$ 120 e R$ 200 (inclusive) | Caro       |
|acima de R$ 200                   | Muito caro |   
-------------------------------------------------

"""
preco = float(input('Iforme o valor do produto: '))

if preco < 50:
    PrecoNovo = preco + (preco * 0.05)
elif preco >= 50 and preco < 100:
    PrecoNovo = preco + (preco * 0.1)
elif preco >= 100:
    PrecoNovo = preco + (preco * 0.15)

if PrecoNovo < 80:
    print(f'Novo Preço = {"%.2f" % PrecoNovo} Barato')
elif PrecoNovo >= 80 and PrecoNovo <= 120:
    print(f'Novo Preço = {"%.2f" % PrecoNovo} Normal')
elif PrecoNovo > 120 and PrecoNovo <= 200:
    print(f'Novo Preço = {"%.2f" % PrecoNovo} Caro')
elif PrecoNovo > 200:
    print(f'Novo Preço = {"%.2f" % PrecoNovo} Muito Caro')
