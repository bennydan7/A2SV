n = int(input())
arr = list(map(int,input().split()))

total_slices = sum(arr)
count = 0
slices = (total_slices // n)

for num in arr:
    if num != slices:
        count += 1
print(count)