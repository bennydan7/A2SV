def find_smallest_k(n, a):
    prefix_product = 1
    total_product = 1
    
    for num in a:
        total_product *= num
    for k in range(1, n):
        prefix_product *= a[k-1]
        suffix_product = total_product // prefix_product
        if prefix_product == suffix_product:
            return k
    
    return -1



t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    results.append(str(find_smallest_k(n, a)))


print("\n".join(results))
