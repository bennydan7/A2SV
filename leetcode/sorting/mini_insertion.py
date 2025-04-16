def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print(*arr) 
            j -= 1
        arr[j + 1] = key
    print(*arr)  

insertionSort([2, 4, 6, 8, 3])