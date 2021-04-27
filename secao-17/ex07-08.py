"""
7) Escreva um código que apresente a classe Circulo, com atributos raio, área e perímetro e,
os métodos calcularArea, calcularPerimetro e imprimir. Os métodos calcularArea e
calcularPerimetro devem efetuar seus respectivos cálculos e colocar os valores nos atributos
area e perimetro. O método imprimir deve mostrar na tela os valores de todos os atributos.
Salienta-se que a área de um círculo é obtida pela fórmula (pi * raio * raio) e o perímetro
por (2 * pi * raio), onde pi = 3,141516.

8) Baseando-se no exercício 7 adicione um método construtor que permita a
definição de todos os atributos no momento da instanciação do objeto.


"""

class Circulo:

    pi = 3.141516

    def __init__(self, raio):
        self.__raio = raio
        self.__area = self.calcularArea
        self.__perimetro = self.calcularPerimetro
    
    @property
    def valor_raio(self):
        return self.__raio

    @property
    def calcularArea(self):
        return self.pi * self.valor_raio ** 2
    
    @property
    def calcularPerimetro(self):
        return 2 * self.pi * self.valor_raio
    
    @property
    def imprimir(self):
        return f'Raio: {self.valor_raio}, Area: {self.__area}, Perimetro: {self.__perimetro} '
