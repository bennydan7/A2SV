def running_sum(nums):
    for i in range(len(nums)):
        nums[i] += nums[i - 1] if i > 0 else 0
    print(nums)


print(running_sum(nums = [1,1,1,1,1]))


def exclusive_sum(nums):
    for i in range(len(nums)):
        nums[i] += nums[i - 2] if i > 0  else 0 
    print(nums)

print(exclusive_sum(nums = [1,1,1,1,1]))