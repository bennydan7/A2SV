t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_sum = 0
    current_max = arr[0]
    
    for i in range(1, n):
        if (arr[i] > 0) != (arr[i - 1] > 0):
            max_sum += current_max
            current_max = arr[i]
        else:
            current_max = max(current_max, arr[i])
    
    max_sum += current_max
    
    print(max_sum)
