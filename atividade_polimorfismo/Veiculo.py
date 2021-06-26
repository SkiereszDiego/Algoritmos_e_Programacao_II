class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade
    
    def imprimir(self):
        print('\nMarca: {} \nQuantidade de Rodas: {} \nModelo: {}\nVelocidade: {}\n'.format (self.marca, self.qtdRodas,self.modelo, self.velocidade))

    def acelerar(self,valor):
        print('Sua velocidade apos acelerar é de: {} Km/h.'.format (valor+self.velocidade))

    def frear(self,valor):
        print('Sua velocidade apos frear é de: {} Km/h.'.format (self.velocidade-valor))