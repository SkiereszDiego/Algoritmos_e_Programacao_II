from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprimeCNPJ(self):
        print("CNPJ: ", self.__cnpj)

    def emitirNotaFiscal(self):
        print('Nota fiscal emitida')

