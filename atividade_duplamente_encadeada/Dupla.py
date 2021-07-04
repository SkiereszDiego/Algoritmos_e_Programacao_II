from random import randint
class Node:
    def __init__(self, dado, anterior):
        self.dado = dado
        self.proximo = None
        self.anterior = anterior

class Dupla:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        self.fim = None

    def adicionar(self, valor):
        if self.inicio:
            cursor = self.inicio
            while cursor.proximo:
                cursor = cursor.proximo
            cursor.proximo = Node(valor, cursor)
            self.fim = cursor.proximo
        else:
            self.inicio = Node(valor, None)
            self.fim = self.inicio
        self.tamanho += 1

    def imprimir(self):
        # if self.tamanho == 0 :
        if self.inicio == None :
            print("Lista vazia!")
        else:
            aux = self.inicio
            while(aux): #(aux != None): 
                print(aux.dado)
                aux = aux.proximo
            print("Tamanho da lista: ", self.tamanho)

    def reverso(self):
        if self.fim == None:
            print("Lista vazia")
        else:
            aux = self.fim
            while aux:
                print(aux.dado)
                aux = aux.anterior
            print("Tamanho da lista: ", self.tamanho)


dupla = Dupla()
dupla.imprimir()
dupla.adicionar(randint(0,99))
dupla.adicionar(randint(0,99))
dupla.imprimir()
dupla.reverso()