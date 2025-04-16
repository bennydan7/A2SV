def find_max_consecutive_ones(nums):
    counter = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            counter += 1
            max_count = max(max_count,counter)
        else:
            counter = 0
    return max_count


print(find_max_consecutive_ones(nums = [1,1,0,1,1,1]))
print(find_max_consecutive_ones(nums = [1,1,0,1,1,0,1,1,1]))