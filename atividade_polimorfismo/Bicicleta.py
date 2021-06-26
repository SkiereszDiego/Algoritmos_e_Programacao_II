from Veiculo import Veiculo

class Bicicleta(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade) 
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimir(self):
        print('\nMarca: {} \nQuantidade de Rodas: {} \nModelo: {}\nVelocidade: {}\nNumero de Marchas: {}\n Bagageiro: {}\n'.format (self.marca, self.qtdRodas, self.modelo, self.velocidade, self.numMarchas, self.bagageiro))


