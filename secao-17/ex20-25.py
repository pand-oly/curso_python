"""
20) Escreva um código que apresente a classe Televisor, com atributos ligado, canal e volume e,
o método imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos.
O atributo ligado será boleano e deverá indicar o estado atual do televisor, se ligado ou
desligado. O atributo canal deverá indicar o canal atual em que o televisor está sintonizado.
O atributo volume deverá indicar o volume atual do televisor.

21) Baseando-se no exercício 20 adicione um método construtor que permita a definição de todos
os atributos no momento da instanciação do objeto.

22) Baseando-se no exercício 21 adicione os métodos ligar e desligar que deverão
mudar o conteúdo do atributo ligado conforme o caso.

23) Baseando-se no exercício 22 adicione os atributos numeroCanais e, volumeMaximo, onde
numeroCanais indica o número máximo de canais que o televisor pode sintonizar e volumeMaximo
indica qual o maior nível de volume possível. O método imprimir deve ser modificado de forma a
mostrar na tela os valores de todos os atributos.

24) Baseando-se no exercício 23 adicione os métodos canalAcima e canalAbaixo, sendo que o
método canalAcima deve sintonizar sempre o próximo canal em relação ao canal atual, onde
ao chegar ao maior canal possível deverá voltar ao canal 1. O método canalAbaixo deve
sintonizar sempre o canal anterior em relação ao canal atual, onde ao chegar ao canal 1
deverá voltar ao maior canal possível, simulando desta forma o funcionamento de um televisor.

25) Baseando-se no exercício 24 adicione os métodos volumeAcima e volumeAbaixo, sendo que o
método volumeAcima deve modificar o volume para o próximo nível de volume possível, onde ao
chegar ao volume Maximo não poderá possibilitar que o volume seja alterado. O método
volumeAbaixo deve modificar o volume para o nível imediatamente inferior de volume em relação
ao volume atual, não podendo ser menor do que 0, simulando desta forma o funcionamento de um
televisor.

"""

class Televisor:

    def __init__(self):
        self.__ligado = False
        self.__canal = 1
        self.__volume = 10

    @property
    def ligado(self):
        if self.__ligado == True:
            return 'ligado'
        return 'desligado'
    
    @property
    def canal(self):
        return f'Canal {self.__canal}'

    @property
    def imprimir(self):
        return f'{self.ligado} - {self.canal} - VOL {self.__volume}'
    
    @staticmethod
    def volumeMaximo():
        volume_maximo = 0
        return volume_maximo
    
    @staticmethod
    def numeroCanais():
        numero_canais = 60
        return numero_canais
    
    def ligar(self):
        self.__ligado = True
    
    def desligar(self):
        self.__ligado = False
    
    def canalAbaixo(self):
        self.__canal -= 1
        if self.__canal < 1:
            self.__canal = Televisor.numeroCanais()
    
    def canalAcima(self):
        self.__canal += 1
        if self.__canal > Televisor.numeroCanais():
            self.__canal = 1
    
    def volumeAcima(self):
        if self.__volume < Televisor.volumeMaximo():
            self.__volume += 1
        else:
            print('Max')

    def volumeAbaixo(self):
        if self.__volume > 0:
            self.__volume -= 1
        else:
            print('Mudo')
