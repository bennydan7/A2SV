class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        if self.head == None:
            return True
        else:
            False

    def pop(self):
        if self.is_empty():
            return -1
        popped_value = self.head.val
        self.head = self.head.next
        return popped_value
    
    def peek(self):
        if self.is_empty():
            return -1
        return self.head.val





