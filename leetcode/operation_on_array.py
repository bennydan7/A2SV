def operation_on_array(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0

    pos = 0
    for i in range(len(nums)):
        if nums[i] !=0:
            nums[pos] = nums[i]
            pos += 1
    while pos < len(nums):
        nums[pos] = 0
        pos += 1
    return nums

print(operation_on_array(nums = [1,0]))
 