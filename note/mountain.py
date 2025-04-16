def mountainArray(arr):
    sorted_array =arr.sort()
    if len(arr) >= 3 and sorted_array == arr:
        return True
    else:
        return False
print(mountainArray(arr = [2,1]))