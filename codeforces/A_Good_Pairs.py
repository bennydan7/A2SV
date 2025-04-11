t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    results = []

    min_element = min(arr)
    max_element = max(arr)

    results.append(arr.index(min_element) +1)
    results.append(arr.index(max_element)+1)
    print(" ".join(map(str,results)))
