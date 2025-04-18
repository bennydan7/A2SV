t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    start = 0
    end = n - 1
    res = []
    while start <= end:
        if start == end:
            res.append(a[start])
        else:
            res.append(a[start])
            res.append(a[end])
        start += 1
        end -= 1
    print(" ".join(map(str, res)))