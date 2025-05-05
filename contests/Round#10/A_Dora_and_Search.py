t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    left, right = 0, n - 1
    min_val = 1
    max_val = n

    while left <= right :
        if arr[left] == min_val:
            left += 1
            min_val += 1
        elif arr[left] == max_val:
            left += 1
            max_val -= 1
        elif arr[right] == min_val:
            right -= 1
            min_val += 1
        elif arr[right] == max_val:
            right -= 1
            max_val -= 1
        else:
            print(left + 1, right + 1)
            break
    else:
        print(-1)
