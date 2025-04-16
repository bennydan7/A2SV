def find_max_average(nums,k):
    initial_average = sum(nums[:k]) / 4
    max_average = 0
    current_sum = 0
    current_average = 0

    left, right = 0,k

    while right < len(nums):
        current_sum = sum(nums[left:right])
        current_average = current_sum / k
        print(current_sum)
        max_average = max(max_average,current_average)
        left += 1
        right += 1
    return max_average
        
        
print(find_max_average(nums = [1,12,-5,-6,50,3], k = 4))
print(find_max_average(nums = [5], k = 1))