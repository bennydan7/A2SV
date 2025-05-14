def crawler_log(logs):
    stack = []

    for element in logs:
        if element == "../" and stack:
            stack.pop()
        elif element == "./":
            continue
        elif element != "../":
            stack.append(element)
    
    return len(stack)

print(crawler_log(logs = ["d1/","d2/","../","d21/","./"]))
print(crawler_log(logs = ["d1/","d2/","./","d3/","../","d31/"]))
print(crawler_log(logs = ["d1/","../","../","../"]))
# print(crawler_log())
# print(crawler_log())