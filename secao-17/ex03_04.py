"""
3) Escreva um código que apresente a classe Quadrado, com atributos lado, área e perímetro e,
os métodos calcularArea, calcularPerimetro e imprimir. Os métodos calcularArea e
calcularPerimetro devem efetuar seus respectivos cálculos e colocar os valores nos atributos area
e perimetro. O método imprimir deve mostrar na tela os valores de todos os atributos. Salienta-se
que a área de um quadrado é obtida pela fórmula (lado * lado) e o perímetro por (4 * lado).

4) Baseando-se no exercício 3 adicione um método construtor que permita a definição de todos os
atributos no momento da instanciação do objeto.

"""

class Quadrado:
    
    def __init__(self, lado):
        self.__lado = lado
        self.__area = self.calcularArea
        self.__perimetro = self.calcularPerimetro
    
    @property
    def valor_lado(self):
       return self.__lado

    @property
    def calcularArea(self):
        return self.valor_lado ** 2
    
    @property    
    def calcularPerimetro(self):
        return 4 * self.valor_lado

    @property
    def imprimir(self):
        return f'lado {self.__lado}, area {self.__area}, perimetro {self.__perimetro} '
