def maxTurbulenceSize(arr):
    n = len(arr)
    right, left = 1,0
    res = 1
    prev = ""

    while right < n :
        if arr[right - 1] > arr[right] and prev != ">":
            res = max(res, right - left + 1)
            right += 1
            prev = ">"
        elif arr[right - 1] < arr[right] and prev != "<":
            res = max(res, right - left + 1)
            right += 1
            prev = "<"
        else:
            right = right + 1 if arr[right] == arr[right - 1] else right
            left = right - 1
            prev = ""
    return res



print(maxTurbulenceSize(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]))  
print(maxTurbulenceSize(arr=[4, 8, 12, 16]))  
print(maxTurbulenceSize(arr=[100]))  
