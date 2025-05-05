n, q = map(int, input().split())
p = list(map(int, input().split()))


p.sort(reverse=True)


prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + p[i - 1]


for _ in range(q):
    x, y = map(int, input().split())
    print(prefix_sum[x] - prefix_sum[x-y])
