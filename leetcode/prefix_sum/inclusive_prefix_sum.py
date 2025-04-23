nums = [-2, 0, 3, -5, 2, -1]

def inclusive_prefix_sum(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]
    return prefix


prefix = inclusive_prefix_sum(nums)

def sumRange(left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]

print(sumRange(0,2))
