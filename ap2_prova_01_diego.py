from abc import ABCMeta, abstractmethod

#COMPUTADOR
class Computador:
    __metaclass__ = ABCMeta
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco 

    @abstractmethod

    def getInformacoes(self):
        print('\nModelo: {} \nCor: {} \nPreco: {}'.format (self.modelo, self.cor, self.preco))
    def cadastrar(self):
        print('cadastro feito com sucesso')

#DESKTOP        
class Desktop(Computador):

    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        Computador.__init__(self, modelo, cor, preco) 
        self._potenciaDaFonte = potenciaDaFonte 

    def getInformacoes(self):
        print('\nMoelo: {} \nCor: {} \nPreco: {} \nPotencia da fonte: {}'.format (self.modelo, self.cor, self.preco, self._potenciaDaFonte))

#NOTEBOOK
class Notebook(Computador):

    def __init__(self, modelo, cor, preco, tempoDeBateria):
        Computador.__init__(self, modelo, cor, preco) 
        self.__tempoDeBateria = tempoDeBateria  

    def getInformacoes(self):
        print('\nMoelo: {} \nCor: {} \nPreco: {} \nTempo de bateria: {}'.format (self.modelo, self.cor, self.preco, self.__tempoDeBateria))

#MAIN
c1 = Computador("Thinkerpad", 'Preto', 4500)
c1.cadastrar()
c1.getInformacoes()

d1 = Desktop('Positivo','Branco', 5700, 550)
d1.getInformacoes()

n1 = Notebook('Dell', "preto", '8500', '4:00')
n1.getInformacoes()
