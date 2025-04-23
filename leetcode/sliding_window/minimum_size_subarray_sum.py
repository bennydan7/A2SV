def minSubArrayLen(nums,target):
    n = len(nums)
    left = 0
    length = float('inf')
    current_sum = 0

    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            length = min(length, right-left+1)
            current_sum -= nums[left]
            left += 1
    if length == float('inf'):
        return 0
    else:
        return length


print(minSubArrayLen(nums=[2,3,1,2,4,3],target=7))
print(minSubArrayLen(nums=[1,4,4],target=4))
print(minSubArrayLen(nums=[1,1,1,1,1,1],target=11))
