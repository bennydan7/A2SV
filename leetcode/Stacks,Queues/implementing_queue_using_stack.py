
class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()

    def empty(self):
        return len(self.list) == 0

    def peek(self):
        if len(self.list) > 0:
            return self.list[-1]
        return None
class MyQueue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def empty(self):
        return self.inStack.empty() and self.outStack.empty()

    def push(self, item):
        self.inStack.push(item)

    def pop(self):
        if self.outStack.empty():
            while not self.inStack.empty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()

    def peek(self):
        if self.outStack.empty():
            while not self.inStack.empty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.peek()
