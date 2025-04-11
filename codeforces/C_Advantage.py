t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    result = []

    sorted_arr = sorted(arr)
    diff_largest = sorted_arr[-2]
    largest_strength = max(arr)
    
    for i in range(n):
        if arr[i] != largest_strength:
            result.append(arr[i] - largest_strength)
        elif arr[i] == largest_strength:
            result.append(largest_strength - diff_largest)
    print(" ".join(map(str,result)))
