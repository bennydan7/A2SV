n,m = map(int,input().split())
n = list(map(int, input().split()))
m = list(map(int,input().split()))

pointer_n = 0
pointer_m = 0

c = []

while pointer_n < len(n) and pointer_m < len(m):
    if m[pointer_m] < n[pointer_n]:
        c.append(m[pointer_m])
        pointer_m += 1
    else:
        c.append(n[pointer_n])
        pointer_n += 1

while pointer_n < len(n):
    c.append(n[pointer_n])
    pointer_n += 1


while pointer_m < len(m):
    c.append(m[pointer_m])
    pointer_m += 1

print(" ".join(map(str, c)))
