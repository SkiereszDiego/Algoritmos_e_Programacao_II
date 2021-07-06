#=-=-=-=-=-=-=-=-=-=-=-=-=-AUTOR-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Autor:
    def __init__(self, id, nome):
        self.__id = id
        self.autor = nome

    def imprimir(self):
        print('ID: {} \nAutor: {}\n'.format (self.__id, self.autor))
    

#=-=-=-=-=-=-=-=-=-=-=-=-=-LIVRO-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=       
class Livro():
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        
    def imprimir(self):
        print('ID: {} \nTitulo: {} \nAutor: {}'.format (self.id, self.titulo, self.autor))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    #=-=-=-=-=-=-=-=-=-=-=-=-=-PIlha-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def adiciona(self, elemento):
        self.dados.append(elemento)
 
    def remove(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0
 
    def imprimir(self):
        if self.dados == []:
            print('Pilha vazia.')
        print(self.dados)
    
############################
    
autor1 = Autor('1', 'Luigi')
autor2 = Autor('2', 'Mario')
autor3 = Autor('3', 'Peach')
autor4 = Autor('4', 'Toad')

print('\n####### Lista de autores #######\n')
autor1.imprimir()
autor2.imprimir()
autor3.imprimir()
autor4.imprimir()

livro1 = Livro('1', 'Lord of the coin', autor1.autor)
livro2 = Livro('2',' Boo madness', autor2.autor)
livro3 = Livro('3', 'Toad wars', autor3.autor)
livro4 = Livro('4', 'Sherlock toad', autor4.autor)

print('\n####### Lista de livros #######\n')
livro1.imprimir()
livro2.imprimir()

livro3.imprimir()
livro4.imprimir()

pilha = Pilha()
pilha.adiciona(livro1.titulo)
pilha.imprimir()
input()
pilha.adiciona(livro2.titulo)
pilha.imprimir()
input()
pilha.adiciona(livro3.titulo)
pilha.imprimir()
input()
pilha.remove()
pilha.imprimir()
input()
pilha.remove()
pilha.imprimir()
input()
pilha.remove()
pilha.imprimir()
