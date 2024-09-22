class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:   #if head not None (mean = null) ,apply new node head and tail to the null
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node   #append new node at the end and apply it to tail
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)  #apply new node at the beginning
        new_node.next = self.head   #(location) put new node at the begin
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def remove(self, value):
        if not self.head:
            return
        if self.head.value == value:    #if the head match the value that wanna remove
            self.head = self.head.next  #set the next node to head and remove the first one
            if not self.head:   # set the tail to the None onstead of null
                self.tail = None
            return
        iterator = self.head
        while iterator.next:
            if iterator.next.value == value:
                iterator.next = iterator.next.next
                if not iterator.next:
                    self.tail = iterator
                return
            iterator = iterator.next

    def iterate(self):
        iterator = self.head  #set iterator from head
        while iterator: # when iterator not null
            print(iterator.value)
            iterator = iterator.next #go to the next node until iteator = null and break

#example
class shoppingcart:
    def __init__(self):
        self.items = LinkedList()

    def add_item(self,item):
        self.items.append(item)

    def delete_item(self,item):
        self.items.remove(item)

    def display_item(self):
        print("The cart including: ")
        self.items.iterate()

cart = shoppingcart()
cart.add_item("apple")
cart.add_item("banana")
cart.add_item("Lemon")
cart.display_item()

cart.delete_item("Lemon")
cart.display_item()
