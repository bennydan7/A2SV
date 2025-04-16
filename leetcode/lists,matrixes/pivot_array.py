def pivotArray(nums,pivot):
    small_nums = []
    big_nums = []
    same_nums = []


    for i in range(len(nums)):
        if nums[i] > pivot:
            big_nums.append(nums[i])
        elif nums[i] < pivot:
            small_nums.append(nums[i])
        elif nums[i] == pivot:
            same_nums.append(nums[i])
    nums = small_nums + same_nums + big_nums
    return nums

print(pivotArray(nums=[9,12,5,10,14,3,10],pivot=10))
print(pivotArray(nums = [-3,4,3,2], pivot = 2))