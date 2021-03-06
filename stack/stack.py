"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   Array is indexed and LinkedList is not. So when using linked list head needs to be assigned and reassigned everytime.
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()

class IsEmptyError(Exception):
    pass

class SLLStack:
    class Node:
        def __init__(self, value, _next):
            self.value = value
            self._next = _next
        
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def push(self, value):
        self.head = self.Node(value,self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IsEmptyError('Stack is empty.')
        result = self.head.value
        self.head = self.head._next
        self.size -= 1
        return result

    def top(self):
        if self.is_empty():
            raise IsEmptyError('Stack is empty. cannot find any first element')
        return self.head.value