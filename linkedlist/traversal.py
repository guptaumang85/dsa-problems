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


l_list = LinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
l_list.head = first
first.next = second
second.next = third

l_list.printList()