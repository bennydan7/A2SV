
# link to problem : https://codeforces.com/contest/2044/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(1,n):
        a = (i,t-1)
        i += 1
        t -= 1
        arr.append(a)
    print(len(arr))
