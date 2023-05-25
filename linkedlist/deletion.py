class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:

  def __init__(self):
    self.head = None

  def printList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

  def deleteNode(self, data):
    temp = self.head
    prev = None

    while temp.data != data:
      prev = temp
      temp = temp.next

    prev.next = temp.next

l_list = LinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
l_list.head = first
first.next = second
second.next = third
third.next = fourth

l_list.printList()

l_list.deleteNode(4)
l_list.printList()