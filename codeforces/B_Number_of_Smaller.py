n,m = map(int,input().split())
n = list(map(int, input().split()))
m = list(map(int,input().split()))

pointer_n = 0
results = []

for number in m:
    while pointer_n < len(n) and n[pointer_n] < number:
        pointer_n += 1
    results.append(pointer_n)

print(" ".join(map(str,results)))
