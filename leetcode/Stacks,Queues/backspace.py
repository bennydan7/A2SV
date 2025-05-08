def backspace(s,t):
    stack_1 = []
    stack_2 = []

    def process(string):
        stack = []
        for element in string:
            if element == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(element)
        return stack

    stack_1 = process(s)
    stack_2 = process(t)
    return stack_1 == stack_2


print(backspace(s = "ab#c", t = "ad#c"))
print(backspace(s = "ab##", t = "c#d#"))
print(backspace( s = "a#c", t = "b"))