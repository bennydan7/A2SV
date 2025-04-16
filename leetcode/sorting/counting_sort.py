def couting_sort(nums):
    maximum = max(nums)
    minimum = min(nums)
    range_of_numbers = maximum - minimum + 1
    count = [0] * range_of_numbers
    print(count)


    # for num in nums:
    #     count[num] += 1
    # target = 0
    # for index, value in enumerate(count):
    #     for i in range(value):
    #         nums[target] = index
    #         target += 1
    # return nums

print(couting_sort(nums = [-2,-3,-5,12,5,1]))