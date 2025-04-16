def countingSort(arr):
    frequency = [0] * 100
    
    for num in arr:
        frequency[num] += 1
    
    return frequency

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements separated by space: ").split()))
    result = countingSort(arr)
    print("Frequency array:", result)