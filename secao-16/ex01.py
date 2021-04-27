"""
1. Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e
altura. Crie os métodos públicos necessários para sets e gets e também um método para imprimir
os dados de uma pessoa.

"""

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    
    def dados_pessoais(self):
        print(f'A(o) {self.__nome}, idade {self.__idade}, altura de {self.__altura}')

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_altura(self):
        return self.__altura
    

eu = Pessoa('Henrique', '23', '1.79')

eu.dados_pessoais()

print(eu.get_nome())
print(eu.get_idade())
print(eu.get_altura())
