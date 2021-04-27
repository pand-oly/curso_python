"""
17) Escreva um código que apresente a classe Eletrodoméstico, com atributo ligado e o método
imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos. O atributo
ligado será boleano e deverá indicar o estado atual do eletrodoméstico, se ligado ou desligado.

18) Baseando-se no exercício 17 adicione um método construtor que permita a definição de todos
os atributos no momento da instanciação do objeto.

19) Baseando-se no exercício 18 adicione os métodos ligar e desligar que deverão
mudar o conteúdo do atributo ligado conforme o caso.

"""

class Eletrodomestico:

    def __init__(self):
        self.__ligado = False
    
    @property
    def ligado(self):
        if self.__ligado == True:
            return 'ligado'
        return 'desligado'
    
    @property
    def imprimir(self):
        return self.ligado

    def ligar(self):
        self.__ligado = True
    
    def desligar(self):
        self.__ligado = False
