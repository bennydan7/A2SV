from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = Counter(a)

    valid = True
    for i in range(1, max(a) + 1):
        if count[i] > count[i - 1]:
            valid = False
            break

    if valid:
        print("YES")
    else:
        print("NO")
    