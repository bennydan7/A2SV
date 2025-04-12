# Read input
n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)

result_indices = []

for i in range(n):
    sum_except_i = total_sum - a[i]
    if sum_except_i == (n - 1) * a[i]:
        result_indices.append(i + 1)

print(len(result_indices))
if result_indices:
    print(" ".join(map(str, result_indices)))


# n = int(input())
# arr = list(map(int, input().split()))
# results = []

# for i in range(n):
#     average_sum = (sum(arr) - arr[i]) / (n - 1)
#     if arr[i] == average_sum:
#         results.append(i + 1)

# if results:
#     print(len(results))
#     print(" ".join(map(str, results)))
# else:
#     print(0)
