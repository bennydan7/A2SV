def sort_the_people(names, heights):
    n = len(names)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if heights[j] > heights[max_idx]:
                max_idx = j
        heights[i], heights[max_idx] = heights[max_idx], heights[i]
        names[i], names[max_idx] = names[max_idx], names[i]

    return names

print(sort_the_people(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
print(sort_the_people(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]))