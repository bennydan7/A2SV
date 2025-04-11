def sort_the_people(names, heights):
    n = len(names)
    for i in range(1, n):
        key = heights[i]
        name_key = names[i]
        j = i - 1
        while j >= 0 and heights[j] < key:  
            heights[j + 1] = heights[j]
            names[j + 1] = names[j]
            j -= 1
        heights[j + 1] = key
        names[j + 1] = name_key
    return names


print(sort_the_people(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
print(sort_the_people(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]))