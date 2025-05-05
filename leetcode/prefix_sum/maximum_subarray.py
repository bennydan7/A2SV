def maximum_subarray(nums):
        prefix_sum = 0
        min_prefix = 0
        max_sum = float('-inf')

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_prefix)
            min_prefix = min(min_prefix, prefix_sum)

        return max_sum

print(maximum_subarray(nums =[-2,1,-3,4,-1,2,1,-5,4]))