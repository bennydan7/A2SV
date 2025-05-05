s = input()
n = len(s)
prefix = [0] * n
for i in range(1, n):
    if s[i] == s[i-1]:
        prefix[i] = prefix[i - 1] + 1
    else:
        prefix[i] = prefix[i - 1]



m = int(input())
results = []
for _ in range(m):
    l, r = map(int, input().split())

    results.append(prefix[r - 1] - prefix[l - 1])


print("\n".join(map(str, results)))
