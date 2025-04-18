t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    a.sort()
    start = 0
    end = n - 1
    count = 0

    while start <= end:
        count += a[end] - a[start]
        start += 1
        end -= 1
    print(count)