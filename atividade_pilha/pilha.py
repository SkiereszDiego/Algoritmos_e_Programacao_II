# Construa um algoritmo para implementação de um Pilha. 
# na Pilha o último elemento adicionado,será o primeiro elemento removido.
# Construa os métodos para inserir e remover elementos da pilha, 
# construa também o método para imprimir a pilha.
import random

class Stack:
    """
    Essa classe implementa a estrutura de dados chamada "pilha"
    """
    def __init__(self):
        self.__stack = []

    def push(self, value):
        """ Adiciona o valor (value) ao final da pilha """
        self.__stack.append(value)

    def pop(self):
        """ Remove o último valor da pilha """
        return self.__stack.pop()

    def show(self):
        """ Imprime a pilha no console """
        print(f'Stack: {self.__stack}')

def main():
    """
    Cria uma pilha e utiliza os métodos show, pop e push
    """
    stack = Stack()

    for _ in range(0, 10):
        stack.push(random.randint(10, 99))
    """
    Mostra valores antes de dar o pop
    """
    stack.show()
    stack.pop()
    stack.pop()
    """
    Mostra valores depois do pop
    """
    stack.show()
    """
    Verifica se a stack esta vazia ou nao
    """
    len(stack)==0
    """
    Verifica qual o elemento do topo da pilha
    """
    stack[-1]

if __name__ == '__main__':
    main()


# OPCIONAL:

# Caso queira inserir por input

# def push():
#   element = input("Digite o elemento: ")
#   stack.append(element)
#   print(stack)

# Caso queira fazer verificacao no delete 

# def pop_element():
#   if not stack:
#     print("stack vazia!")
#   else:
#     e = stack.pop()
#     print("remove o elemento:", e)
#     print(stack)