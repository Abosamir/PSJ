class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def list_length(self):
        current_node = self.head
        length = 0
        while current_node:
            current_node = current_node.next
            length +=1
        return length

    def insert_at_beginning(self, node):
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            node.next = current_node
            self.head = node

    def insert(self,node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def insert_at(self, node, position):

        if position < 0 or position > self.list_length():
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_beginning(node)
            return

        current_node = self.head
        i = 0
        while i != position-1:
            current_node = current_node.next
            i += 1
        later_node = current_node.next
        current_node.next = node
        node.next = later_node

    def delete_at_end(self):
        current_node = self.head
        length_of_list = self.list_length()
        i = 0
        while i != length_of_list-2:
            current_node = current_node.next
            i += 1
        current_node.next = None
    
    def delete_at(self, position):
        
        current_node = self.head
        if position == 0:
            self.head = current_node.next
            return
        
        if position <0 or position >= self.list_length():
            print("Invalid Position")
            return

        i = 0
        while i!= position:
            previous_node = current_node
            current_node = current_node.next
            i += 1
        previous_node.next = current_node.next

    def print(self):
        if self.head:
            current_node = self.head
            while current_node:
                print(current_node.data,"------>",end="")
                current_node=current_node.next
        else:
            print("List is empty")

first_node = Node("mohamed")
second_node = Node("osama")
third_node = Node("samir")
fourth_node = Node("yassmin")
fifth_node = Node("yassin")
ll = LinkedList()
ll.insert(first_node)
ll.insert(second_node)
ll.insert(third_node)
ll.insert_at_beginning(fourth_node)
ll.insert_at(fifth_node,0)
ll.delete_at(-1)
ll.print()