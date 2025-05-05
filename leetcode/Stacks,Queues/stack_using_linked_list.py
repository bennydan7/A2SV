class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
print(stack.peek())  # Output: 10