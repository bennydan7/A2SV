def count_pairs(nums,k):
    n = len(nums)
    result = []
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] == nums[j] and (i * j) % k ==0:
                result.append((nums[i],nums[j]))
    return len(result)
    

print(count_pairs(nums = [3,1,2,2,2,1,3], k = 2))
print(count_pairs(nums = [1,2,3,4], k = 1))