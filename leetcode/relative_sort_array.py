from collections import defaultdict

def relative_sort(arr1,arr2):
    arr1_count = {x: 0 for x in arr1}
    end = []
    for num in arr1:
        if num not in arr2:
            end.append(num)
        arr1_count[num] += 1
    end.sort()
    
    res = []
    for num in arr2:
        for _ in range(arr1_count[num]):
            res.append(num)
    return res + end




    


print(relative_sort(arr1=[28,6,22,8,44,17],arr2=[22,28,8,6]))