from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortasCarro):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor) 
        self.qtdPortas = qtdPortasCarro

    def imprimir(self):
        print('\nMarca: {} \nQuantidade de Rodas: {} \nModelo: {}\nVelocidade: {}\n Potenci do Motor: {}\n Portas: {}\n'.format (self.marca, self.qtdRodas, self.modelo, self.velocidade, self.potenciaDoMotor, self.qtdPortas))

