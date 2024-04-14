class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def print(self):
        if self.head:
            current_node = self.head
            while current_node:
                print(current_node.data,"------>",end="")
                current_node=current_node.next
        else:
            print("List is empty")
    
    def insert_at_beginning(self, node):
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            node.next = current_node
            self.head = node



first_node = Node("mohamed")
second_node = Node("osama")
third_node = Node("samir")
fourth_node = Node("yassmin")
ll = LinkedList()
ll.insert(first_node)
ll.insert(second_node)
ll.insert(third_node)
ll.insert_at_beginning(fourth_node)
ll.print()