def pancake_sorting(arr):

    def flip(end):
        start = 0 
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
    n = len(arr)
    output = []

    for i in range(n-1,-1,-1):
        max_element = i
        for j in range(i,-1,-1):
            if arr[j] > arr[max_element]:
                max_element = j
        if max_element != i:
            flip(max_element)
            flip(i)
            output.append(max_element + 1)
            output.append(i + 1)
    return output


print(pancake_sorting(arr=[3,2,4,1]))
print(pancake_sorting(arr=[1,3,2]))

