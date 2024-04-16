# There are three methods to implement stack in python

# first we can use list as a stack

# -------------------------------------
s = []
s.append("Mohamed")
s.append("Osama")
s.append("Yassmin")
s.append("Yassin")
print(s)
print(s.pop()) # this method has two effects return the element and remove it.
print(s)
# -------------------------------------

# Second method is using Collection.deque

# -------------------------------------
from collections import deque

stack = deque()

stack.append("Mohamed")
stack.append("Osama")
stack.append("Yassmin")
stack.append("Yassin")

print(stack)
print(stack.pop())
print(stack)
# -------------------------------------

# Third method is by creating our stack class on top of deque

from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, element):
        self.container.append(element)

    def peak(self):
        return self.container[-1]
    
    def pop(self):
        return self.container.pop()
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    

stack = Stack()

stack.push("Mohamed")
stack.push("Osama")
stack.push("Yassmin")
stack.push("Yassin")

print(stack.peak())
print(stack.pop())
# -------------------------------------