def  removing_stars_from_string(s):
    stack = []

    for char in s:
        if char == '*' and stack:
                stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)

print(removing_stars_from_string(s = "leet**cod*e"))
print(removing_stars_from_string( s = "erase*****"))