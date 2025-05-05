def subarray_sums_divisble(nums,k):
    count = 0
    dict = {0 : 1}

    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]
    for i in range(1,len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    
    
    # for num in nums:




print(subarray_sums_divisble(nums = [4,5,0,-2,-3,1], k = 5))