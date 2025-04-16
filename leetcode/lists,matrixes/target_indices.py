def target_indices(nums,target):
    target_indices = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            target_indices.append(i)
    return target_indices


print(target_indices(nums = [1,2,5,2,3], target = 2))
print(target_indices(nums = [1,2,5,2,3], target = 3))
print(target_indices(nums = [1,2,5,2,3], target = 2))