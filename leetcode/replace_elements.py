def replace_elements(arr):
    n = len(arr)
    if n == 0:
        return []
    max_element = -1

    for i in range(n-1,-1,-1):
        temp = arr[i]
        arr[i] = max_element
        if temp > max_element:
            max_element = temp
        print(arr)
    
    return arr
    

print(replace_elements(arr = [17,18,5,4,6,1]))