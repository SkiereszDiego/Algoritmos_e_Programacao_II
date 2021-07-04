from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def append(self, elem):
    if self.head:
      #insere qndo a lista ja possui elementos
      pointer = self.head
      while(pointer.next):
        pointer = pointer.next
      pointer.next = Node(elem)
    else:
      #primeira insercao
      self.head = Node(elem)

lista = LinkedList()