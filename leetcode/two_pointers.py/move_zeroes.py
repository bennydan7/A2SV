def move_zeros(nums):
    seeker = 0
    placeholder = 0
    while seeker < len(nums):
        if nums[seeker] != 0:
            nums[placeholder], nums[seeker] = nums[seeker], nums[placeholder]
            placeholder += 1
        seeker += 1
    return nums

print(move_zeros(nums = [0,1,0,3,12]))