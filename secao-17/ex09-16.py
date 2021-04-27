"""
9) Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor e marcha e,
o método imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos. O
atributo marcha indica em que a marcha a Moto se encontra no momento, sendo representado de
forma inteira, onde 0 - neutro, 1 – primeira, 2 – segunda, etc.

10) Baseando-se no exercício 9 adicione um método construtor que permita a definição de todos
os atributos no momento da instanciação do objeto.

11) Baseando-se no exercício 10 adicione os métodos marchaAcima e marchaAbaixo que deverão
efetuar a troca de marchas, onde o método marchaAcima deverá subir uma marcha, ou seja, se
a moto estiver em primeira marcha, deverá ser trocada para segunda marcha e assim por diante.
O método marchaAbaixo deverá realizar o oposto, ou seja, descer a marcha. O método imprimir
deve ser modificado de forma a mostrar na tela os valores de todos os atributos.

12) Baseando-se no exercício 11 adicione os atributos menor Marcha e maior Marcha, onde o
atributo menorMarcha indica qual será a menor marcha possível para a moto e o atributo
maiorMarcha indica qual será a maior marcha possível. Desta forma os métodos marchaAcima e
marchaAbaixo devem ser reescritos de forma a não permitirem a troca de marchas para valores
abaixo da menorMarcha e acima da maiorMarcha. O método imprimir deve ser modificado de forma
a mostrar na tela os valores de todos os atributos.

13) Baseando-se no exercício 12 adicione um método construtor que permita a definição de todos
os atributos no momento da instanciação do objeto.

14) Baseando-se no exercício 13 adicione o atributo ligada que terá a função de indicar se a
moto está ligada ou não. Este atributo deverá ser do tipo boleano. O método imprimir deve ser
modificado de forma a mostrar na tela os valores de todos os atributos.

15) Baseando-se no exercício 14 adicione um método construtor que permita a definição de todos
os atributos no momento da instanciação do objeto.

16) Baseando-se no exercício 15 adicione os métodos ligar e desligar que deverão mudar o
conteúdo do atributo ligada conforme o caso.

"""

class Moto:

    def __init__(self, marca, modelo, cor):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = -1
        self.__ligada = False
    
    @property
    def marcha(self):
        if self.__marcha == 0:
            return 'Neutro'
        elif self.__marcha == 1:
            return 'Primeira'
        elif self.__marcha == 2:
            return 'Segunda'
        elif self.__marcha == 3:
            return 'Terceira'
        elif self.__marcha == 4:
            return 'Quarta'
        elif self.__marcha == 5:
            return 'Quinta'
        else:
            return 'Morto'

    @property
    def ligar(self):
        self.__ligada = True
        return self.__ligada
    
    @property
    def desligar(self):
        self.__ligada = False

    @property
    def maiorMarcha(self):
        MaiorMarcha = 5
        return MaiorMarcha

    @property
    def menorMarcha(self):
        MenorMarcha = 0
        return MenorMarcha

    @property
    def imprimir(self):
        return (f'{self.__marca} - {self.__modelo} - {self.__cor} - {self.marcha} marcha -' +
                    f' ligada {self.__ligada}')

    def marchaAcima(self):
        if self.__marcha < self.maiorMarcha:
            self.__marcha += 1

    def marchaAbaixo(self):
        if self.__marcha > self.menorMarcha:
            self.__marcha -= 1
