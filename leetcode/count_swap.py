def countSwaps(a):
    n = len(a)
    numSwaps = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1
    firstElement = a[0]
    lastElement = a[-1]
    print(f"Array is sorted in {numSwaps} swaps")
    print(f"First Element: {firstElement}")
    print(f"Last Element: {lastElement}")


print(countSwaps(a=[6,4,1]))
print(countSwaps(a=[1,2,3]))