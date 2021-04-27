"""
1) Escreva um código que apresente a classe Pessoa, com atributos nome, endereço e telefone e,
o método imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos.


2) Baseando-se no exercício 1 adicione um método construtor que permita a definição de todos
os atributos no momento da instanciação do objeto.


"""
class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    @property
    def imprimir(self):
        return f'{self.nome}: {self.endereco}, {self.telefone}'
