from Veiculo import Veiculo

class Automovel(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade) 
        self.potenciaDoMotor = potenciaDoMotor
        
    def imprimir(self):
        print('\nMarca: {} \nQuantidade de Rodas: {} \nModelo: {}\nVelocidade: {}\n Potencia do Motor: {}\n'.format (self.marca, self.qtdRodas, self.modelo, self.velocidade, self.potenciaDoMotor))

