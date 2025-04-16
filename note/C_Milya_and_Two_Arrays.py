t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    distinct_a = len(set(a))
    distinct_b = len(set(b))
    
    if distinct_a >= 2 and distinct_b >= 2:
        print("YES")
    elif distinct_a >= 3 or distinct_b >= 3:
        print("YES")
    else:
        combined = set()
        for i in range(n):
            combined.add(a[i] + b[i])
        if len(combined) >= 3:
            print("YES")
        else:
            print("NO")