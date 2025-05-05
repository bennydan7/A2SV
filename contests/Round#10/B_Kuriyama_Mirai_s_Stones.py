n = int(input())
v = list(map(int,input().split()))
m = int(input())

original_prefix_sum = [0] * (n + 1)
sorted_prefix_sum = [0] * (n + 1)

v_sorted = sorted(v)
for i in range(1, n + 1):
    original_prefix_sum[i] = original_prefix_sum[i - 1] + v[i - 1]
    sorted_prefix_sum[i] = sorted_prefix_sum[i - 1] + v_sorted[i - 1]

for _ in range(m):
    t,l,r = list(map(int,input().split()))
    if t == 1:
        print(original_prefix_sum[r] - original_prefix_sum[l - 1] )
    else:
        print(sorted_prefix_sum[r] - sorted_prefix_sum[l - 1])
