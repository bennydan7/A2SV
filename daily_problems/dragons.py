
s,n = map(int, input().split())
pairs = []
for _ in range(n):
    x,y = map(int,input().split())
    pairs.append((x,y))

pairs.sort()

for x,y in pairs:
    if s > x:
        s +=y
    else:
        print("NO")
        break
else:
    print("YES")
    


