"""
26) Escreva um código que apresente a classe Microondas, com atributo ligado e o método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos. O atributo ligado será
boleano e deverá indicar o estado atual do microondas, se ligado ou desligado.

27) Baseando-se no exercício 26 adicione um método construtor que permita a
definição de todos os atributos no momento da instanciação do objeto.

28) Baseando-se no exercício 27 adicione os métodos ligar e desligar que deverão
mudar o conteúdo do atributo ligado conforme o caso.

29) Baseando-se no exercício 28 adicione o atributo portaFechada que deverá ser boleano e deverá
indicar se a porta do microondas está ou não fechada. O método imprimir deve ser modificado de
forma a mostrar na tela os valores de todos os atributos.

30) Baseando-se no exercício 29 adicione os métodos fecharPorta e abrirPorta que
deverá mudar o conteúdo do atributo portaFechada conforme o caso.

31) Baseando-se no exercício 30 modifique o método ligar para que só ligue o equipamento quando
a porta do mesmo estiver fechada, simulando assim o funcionamento de um microondas.

"""

class Microondas:

    def __init__(self):
        self.__ligado = False
        self.__porta = True
    
    @property
    def ligado(self):
        if self.__ligado == True:
            return 'On'
        return 'Off'
    
    @property
    def portaFechada(self):
        if self.__porta == True:
            return 'Porta esta fechada'
        return 'Porta esta aberta'
    
    @property
    def imprimir(self):
        return f'{self.ligado} - {self.portaFechada}'
    
    def ligar(self):
        if self.__porta == True:
            self.__ligado = True
        else:
            print('feche a porta para ligar')
    
    def desligar(self):
        self.__ligado = False
    
    def abrirPorta(self):
        self.__porta = False
        self.__ligado = False
    
    def fecharPorta(self):
        self.__porta = True
