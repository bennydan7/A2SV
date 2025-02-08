import math

def perfect_square(x):
    if x < 0:
        return False
    y = int(math.sqrt(x))
    return y * y == x

def largest_non_perfect_square(arr):
    largest = -float('inf')
    for num in arr:
        if not perfect_square(num):
            largest = max(largest, num)
    return largest
    
n = int(input())
arr = list(map(int,input().split()))
print(largest_non_perfect_square(arr))