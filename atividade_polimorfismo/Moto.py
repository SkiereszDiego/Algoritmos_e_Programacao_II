from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor) 
        self.partidaEletrica = partidaEletrica

    def imprimir(self):
        print('\nMarca: {} \nQuantidade de Rodas: {} \nModelo: {}\nVelocidade: {}\n Potencia do Motor: {}\n Partida Eletrica: {}\n '.format (self.marca,
            self.qtdRodas, self.modelo, self.velocidade, self.partidaEletrica, self.potenciaDoMotor))

