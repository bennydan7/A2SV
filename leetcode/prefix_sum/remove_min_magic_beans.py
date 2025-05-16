def minimumRemoval(beans):
    beans.sort()
    total_beans = sum(beans)
    n = len(beans)
    min_removal = float('inf')

    for i in range(n):
        keep = beans[i] * (n - i)
        min_beans = total_beans - keep
        min_removal = min(min_removal,min_beans)
    return min_removal
        
print(minimumRemoval( beans = [4,1,6,5]))