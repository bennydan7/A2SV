def subarray_sums_divisble(nums,k):
    count = 0
    remainder_count = {0 : 1}

    prefix_sum = 0
    
    
    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k

        if remainder < 0 :
            remainder += k
        
        count += remainder_count.get(remainder,0)

        remainder_count[remainder] = dict.get(remainder,0) + 1

    return count




print(subarray_sums_divisble(nums = [4,5,0,-2,-3,1], k = 5))