"""
2. Crie uma classe Pessoa que pode armazenaPessoa 10 pessoas e seja capas de realizar as
seguintes operações:

• void armazenaPessoa(String nome, int idade, float altura); 
• void removePessoa(String nome);
• int buscaPessoa(String nome); // informa em que posição da agenda está a pessoa
• void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda
• void imprimePessoa(int index); // imprime os dados da pessoa que está na posição “i” da agenda.

"""

class Agenda:

    lista = dict()

    @classmethod
    def removePessoa(cls, quem):
        try:
            del cls.lista[quem]
            print('Agenda Atualizada.')
        except KeyError:
            print('Pessoa inexistente nesta agenda')

    @classmethod
    def buscaPessoa(cls, quem):
        try:
            busca = cls.lista[quem]
            print(f'{busca[0]} {quem}')
        except KeyError:
            print('Pessoa inexistente nesta agenda')

    @classmethod
    def imprimePessoa(cls, quem):
        try:
            busca = cls.lista[quem]
            print(busca)
        except KeyError:
            print('Pessoa inexistente nesta agenda')

    @staticmethod
    def imprimeAgenda():
        try:
            with open('ex02_Agenda.txt', 'r') as arquivo:
                print(arquivo.read())
        except FileNotFoundError:
            print('Nenhum dado foi cadastrado na agenda até o momento!')

    def __init__(self, posicao, nome, idade, altura):
        self.__posicao = f'Posição {posicao}'
        self.__nome = nome
        self.__idade = f'{idade} anos.'
        self.__altura = f'altura : {altura}'
    
    def armazenaPessoa(self):
        Agenda.lista[self.__nome]= [self.__posicao, self.__idade, self.__altura]
        with open('ex02_Agenda.txt', 'a') as arquivo:
            arquivo.write(f'{self.__nome} = {self.__posicao}, {self.__idade}, {self.__altura}\n')


for i in range(1, 4):
    posicao = i
    try:
        nome = str(input(f'{i} - Digite nome da pessoa: '))
    except ValueError:
        nome = 'Dado iserido incorreto'

    try:
        idade = int(input(f'{i} - Informe sua idade: '))
    except ValueError:
        idade = 'Dado iserido incorreto'

    try:
        altura = float(input(f'{i} - E sua altura: '))
    except ValueError:
        altura = 'Dado iserido incorreto'
    
    pessoa = Agenda(posicao, nome, idade, altura)
    pessoa.armazenaPessoa()

menu = int(input('Digite uma das opções:\n 1- Remover uma pessoa:\n 2- Buscar uma pessoa:\n '+
                  '3- Imprimir agenda:\n 4- Imprimir dados de uma pessoa:\n 5- Caso deseja sair. '
                  ))

if menu == 1:
    quem = str(input('Digite o nome da pessoa que deseja remover: '))
    Agenda.removePessoa(quem)
elif menu == 2:
    quem = str(input('Digite o nome da pessoa que deseja buscar: '))
    Agenda.buscaPessoa(quem)
elif menu == 3:
    Agenda.imprimeAgenda()
elif menu == 4:
    quem = str(input('Digite o nome da pessoa que deseja buscar os dados: '))
    Agenda.imprimePessoa(quem)
elif menu == 5:
    exit(1)
else:
    print('Número invalido')
    