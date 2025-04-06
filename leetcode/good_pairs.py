def numIdenticalPairs(nums):
    n = len(nums)
    results = []
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] == nums[j] and i < j:
                results.append((nums[i],nums[j]))
    return len(results)
                
print(numIdenticalPairs(nums = [1,2,3,1,1,3]))
print(numIdenticalPairs(nums = [1,2,3]))