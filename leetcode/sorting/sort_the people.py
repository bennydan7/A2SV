def sort_the_people(names,heights):
    n = len(names)
    for i in range(n-1):
        for j in range(n-1):
            if heights[j] < heights[j+1]:
                heights[j], heights[j+1] = heights[j+1], heights[j]
                names[j], names[j+1] = names[j+1], names[j]
    return names

print(sort_the_people(names = ["Mary","John","Emma"], heights = [180,165,170]))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

    