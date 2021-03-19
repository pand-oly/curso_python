"""
34. Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor. Os dados
deverão ser armazenados no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite
um número que já foi digitado anteriormente, o programa devera pedir para ele digitar outro número.
Note que cada valor digitado pelo usuário deve ser pesquisado no vetor, verificando se ele
existe entre os números que já foram fornecidos. Exibir na tela o vetor final que foi digitado.

"""

vetor = []
while len(vetor) < 10:
    num = int(input('Informe um número para o vetor: '))
    if num in vetor:
        num = int(input('Repetiu informe novamente um número: '))
    else:
        vetor.append(num)

print(vetor)