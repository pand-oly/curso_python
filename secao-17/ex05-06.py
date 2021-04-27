"""
5) Escreva um código que apresente a classe Retângulo, com atributos comprimento, largura, área
e perímetro e, os métodos calcularArea, calcularPerimetro e imprimir. Os métodos calcularArea e
calcularPerimetro devem efetuar seus respectivos cálculos e colocar os valores nos atributos
area e perimetro. O método imprimir deve mostrar na tela os valores de todos os atributos.
Salienta-se que a área de um retângulo é obtida pela fórmula (comprimento * largura) e o
perímetro por (2 * comprimento) + (2 * largura).

6) Baseando-se no exercício 5 adicione um método construtor que permita a
definição de todos os atributos no momento da instanciação do objeto.


"""

class Retangulo:

    def __init__(self, comprimento, largura):
        self.__comprimeto = comprimento
        self.__largura = largura
        self.__area = self.calcularArea
        self.__perimetro = self.calcularPerimetro
    
    @property
    def valor_comprimento(self):
        return self.__comprimeto
    
    @property
    def valor_largura(self):
        return self.__largura  

    @property
    def calcularArea(self):
        return self.valor_comprimento * self.valor_largura
    
    @property
    def calcularPerimetro(self):
        return (2 * self.valor_comprimento) + (2 * self.valor_largura)
    
    @property
    def imprimir(self):
        return (f'comprimento: {self.valor_comprimento}, largura: {self.valor_largura}, '
                f'area: {self.__area}, perímetro: {self.__perimetro} ')
