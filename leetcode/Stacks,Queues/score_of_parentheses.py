def score_of_parentheses(s):
    stack = []
    for element in s:
        if element == '(':
            stack.append(element)
        elif element == ')':
            score = 0
            while stack and isinstance(stack[-1],int):
                score += stack.pop()
            stack.pop()

            if score == 0:
                stack.append(1)
            else:
                stack.append(2 * score)
    return sum(stack)


