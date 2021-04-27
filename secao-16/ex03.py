"""
3. Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um
prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio, excluindo
o térreo, capacidade do elevador, e quantas pessoas estão presentes nele.

A classe deve também disponibilizar os seguintes métodos:

 • Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no
   prédio (os elevadores sempre começam no térreo e vazio);

 • Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);

 • Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);

 • Sobe: para subir um andar (não deve subir se já estiver no último andar);

 • Desce: para descer um andar (não deve descer se já estiver no térreo);

 • Encapsular todos os atributos da classe (criar os métodos set e get).

"""

class Elevador:

    andar_atual = 0
    carga = 0

    def __init__(self, total_andares, capacidade_elevador):
       self.__andar_atual = Elevador.andar_atual
       self.__total_andares = total_andares
       self.__capacidade_elevador = capacidade_elevador
       self.__carga = Elevador.carga
  
  
    def verifica_capacidade(self):
       return self.__capacidade_elevador    
    
    def verifica_carga(self):
       return self.__carga
     
    def verifica_andar(self):
       return self.__andar_atual
    
    def verifica_andares(self):
       return self.__total_andares

   
    def entrar(self, quantidade):
        if (quantidade + self.verifica_carga()) <= self.verifica_capacidade():
            self.__carga += quantidade
            print(f'Entrou {quantidade} pessoa(s)')
        else:
             sobrou = (quantidade + self.verifica_carga()) - self.verifica_capacidade()
             entrou = quantidade - sobrou
             if entrou == 0:
                 print('Elevador cheio espere o proximo')
             else :
                 self.__carga += entrou
                 print(f'Entrou {entrou} pessoa(s) e {sobrou} aguarde o proximo elevador')
    

    def sair(self, quantidade):
        if self.verifica_carga() > 0:
            if quantidade > self.verifica_carga():
                quantidade = self.verifica_carga()
           
            self.__carga -= quantidade
            print(f'Saiu {quantidade} do elevador, restam {self.verifica_carga()}')
        else:
            print('Elevador vazio')
    

    def subir(self, quantidade):
        if (quantidade + self.verifica_andar()) <= self.verifica_andares():
            self.__andar_atual += quantidade
            print(f'O elevador subiu para o {self.verifica_andar()}° andar')
        else:
            sobrou = (quantidade + self.verifica_andar()) - self.verifica_andares()
            subiu = quantidade - sobrou
            if subiu == 0:
                print('Ultimo andar')
            else :
                self.__andar_atual += subiu
                print(f'O elevador subiu para o {self.verifica_andar()}° andar')
                
   
    def descer(self, quantidade):
        if self.verifica_andar() > 0:
            if quantidade > self.verifica_andar():
                quantidade = self.verifica_andar()
            self.__andar_atual -= quantidade
            print(f'O elevador desceu para o {self.verifica_andar()}° andar')
        else:
            print('terrio')


menu = input('Click Enter para iniciar')

try:
    iniciar = Elevador(int(input('Digite total de andares: ')),
                        int(input('Digite a capacidade do elevador: ')))
except ValueError:
   print('Valor incorreto execulte novamente: ')

while menu != 5:

    try:
       menu = int(input('Digite uma das opções:\n'+
                         ' 1- Entrar:\n 2- Sair:\n 3- Subir:\n 4- Descer:\n 5- Encerrar: '))
    except ValueError:
       menu = 5
       print('Valor incorreto execulte novamente: ')
    
    if menu == 1:
        quant_entrou = int(input('Digite a quantidade de pessoas que vão entrar no elevador: '))
        iniciar.entrar(quant_entrou)
    elif menu == 2:
        quant_sair = int(input('Digite quantas pessoas sairam: '))
        iniciar.sair(quant_sair)
    elif menu == 3:
        subir_quant = int(input('Digite quantos andares elevador vai subir: '))
        iniciar.subir(subir_quant)
    elif menu == 4:
        descer_quant = int(input('Digite quantos andares elevador vai descer: '))
        iniciar.descer(descer_quant)
    elif menu == 5:
       print('Fim do programa.')
       exit(4)
