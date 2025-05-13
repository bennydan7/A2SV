def evaluate_reverse_polish_notation(tokens):
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            if token == "-":
                stack.append(a - b)
            if token == "*":
                stack.append(a * b)
            if token == "/":
                stack.append(int(a / b)) 
    return stack[0]


