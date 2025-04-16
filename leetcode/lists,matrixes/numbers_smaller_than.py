def many_numbers_smaller(nums):
    n = len(nums)
    result = []
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] > nums[j]:
                count += 1
        result.append(count)
    return result


print(many_numbers_smaller(nums = [8,1,2,2,3]))