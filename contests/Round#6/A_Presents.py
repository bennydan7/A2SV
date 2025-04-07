n = int(input())
arr = list(map(int,input().split()))
presents = [0] * n
for i in range(n):
    presents[arr[i] - 1] = i + 1
print(" ".join(map(str, presents)))