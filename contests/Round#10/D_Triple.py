t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    res = {}
    if len(arr) < 3:
        print(-1)
        continue
    
    found = -1
    for num in arr:
        if num in res:
            res[num] += 1
        else:
            res[num] = 1
        if res[num] == 3:
            found = num
            break
    print(found)
    