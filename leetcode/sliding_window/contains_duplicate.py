def contains_duplicate(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False

print(contains_duplicate(nums=[1, 2, 3, 1, 2, 3], k=2))