def exclusive_prefix_sum(nums):
    accumulator = 0
    for i in range(len(nums) + 1):
        accumulator += nums[i]
        accumulator = 0
    print(nums)
         

print(exclusive_prefix_sum(nums = [1,1,1,1,1]))
