"""
4. Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume
e trocar os canais da televisão.

• O controle de volume permite aumentar ou diminuor a potência do volume de som em uma unidade de
cada vez;

• O controle de canal também permite aumentar e diminuir o número do em uma unidade,
porém, também possibilita trocar para um canal indicado

• Também devem ecistir métodos para consultar o valor do volume de som canal selecionado.

"""

class Televisao:

    def __init__(self):
        self.__canal = 1
        self.__volume = 1 

    def consulta_canal(self):
        return self.__canal
    
    def consulta_volume(self):
        return self.__volume

    def regula_volume(self, dado):
        if self.__volume > 0:
            self.__volume = self.__volume + dado
            if self.__volume > 10:
                self.__volume = 10
                print('Max') 
        else:
            print('Mudo')
        
        print(ControleRemoto.consulta_volume(self))
    
    def novo_canal(self, dado):
        if dado == 0:
            self.__canal += 1
        else:
            if dado == -1:
                self.__canal += dado
            else:
                self.__canal = dado
        print(ControleRemoto.consulta_canal(self))


    
class ControleRemoto:

    @staticmethod
    def almentar_volume(console):
        console.regula_volume(+1)

    @staticmethod
    def diminuir_volume(console):
        console.regula_volume(-1)

    @staticmethod
    def mudar_canal(console, dado=0):
        console.novo_canal(dado)
    
    @staticmethod
    def down_chanel(console):
        console.novo_canal(-1)
    
    @staticmethod
    def consulta_canal(console):
        return f'Canal {console.consulta_canal()}'
    
    @staticmethod
    def consulta_volume(console):
        return f'Volume: {console.consulta_volume()}0%'


tv = Televisao()

ControleRemoto.almentar_volume(tv)
ControleRemoto.diminuir_volume(tv)
ControleRemoto.mudar_canal(tv)
ControleRemoto.mudar_canal(tv, 20)
ControleRemoto.down_chanel(tv)
