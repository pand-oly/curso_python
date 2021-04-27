from random import randint

class Calcular:

    def __init__(self, dificuldade: int) -> None:
        self.__dificuldade = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 4)
        self.__resultado: int = self._gerar_resultado
    
    @property
    def dificuldade(self) -> int:
        return self.__dificuldade
    
    @property
    def valor1(self) -> int:
        return self.__valor1

    @property
    def valor2(self) -> int:
        return self.__valor2

    @property
    def operacao(self) -> int:
        return self.__operacao

    @property
    def resultado(self) -> int:
        return self.__resultado
    
    def __str__(self) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        elif self.operacao == 4:
            op = 'Dividir'
        else:
            op = 'Erro na operação'
        return (f'Valor 1: {self.valor1} \nValor 2: {self.valor2}\n'+
                  f'Dificulade: {self.dificuldade} \nOperação: {op}')
        
    @property
    def _gerar_valor(self) -> int:
        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(1, 100)
        elif self.dificuldade == 3:
            return randint(1, 1000)
        else:
            return randint(1, 10000)
        
    
    @property
    def _gerar_resultado(self) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        elif self.operacao == 3:
            return self.valor1 * self.valor2
        else:
            return self.valor1 / self.valor2
    
    @property
    def _str_op(self) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        else:
            return '/'
    
    def checar_resultado(self, resposta) -> bool:
        verifc: bool = False

        if self.resultado == resposta:
            print('Resposta Correta!')
            verifc = True
        else:
            print('Errou! :p')
        
        print(f'{self.valor1} {self._str_op} {self.valor2} = {self.resultado}')
        return verifc
    
    def mostrar_operacao(self) -> None:
        print(f'{self.valor1} {self._str_op} {self.valor2} = ?')
