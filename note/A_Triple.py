def find_triplet_occurrences(t, test_cases):
    results = []
    for n, arr in test_cases:
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] >= 3:
                results.append(num)
                break
        else:
            results.append(-1)
    return results


# Input handling
t = int(input())  # Number of test cases
test_cases = []

for _ in range(t):
    n = int(input())  # Length of the array
    arr = list(map(int, input().split()))  # Array elements
    test_cases.append((n, arr))

# Solve and print results
results = find_triplet_occurrences(t, test_cases)
print("\n".join(map(str, results)))