"""
8. Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo,
mas com todas as letras minúsculas convertidas para maiúsculas. Os nomes dos arquivos serão
fornecidos, via teclado, pelo usuário. A função que converte maiúscula para minúscula é o
toupper(). Ela é aplicada em cada caractere da string.

"""

fil = input('Digite nome do arquivo: ')
name, expansion = fil.split('.')

with open(f'{name + "-01." + expansion}', 'a') as new:
    with open(fil, 'r') as fil:
        for i in fil.read():
            new.write(i.upper())  # toupper() é obsoleto desde a versão 3.3 do python 
