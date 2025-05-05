def count_good_pairs(n, a, b):
    c = [a[i] - b[i] for i in range(n)]
    c.sort()
    
    count = 0
    j = n - 1
    
    for i in range(n):
        if c[i] <= 0:
            continue
        # move j leftward to find first c[j] such that c[i] + c[j] > 0
        while j >= 0 and c[i] + c[j] > 0 and j >= i:
            j -= 1
        count += i - (j + 1)
        
    return count

# Example usage:
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(count_good_pairs(n, a, b))
