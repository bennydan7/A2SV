t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n % 2 == 0 or k % 2 == 1:  
        print("YES")
    else:
        print("NO")

