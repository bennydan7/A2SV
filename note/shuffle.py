def shuffle_array(n,nums):
    mid = len(nums) // 2
    first_half = nums[:mid]
    second_half = nums[mid:]
    print(first_half,second_half)
    answer = []
    for i in range(n):
        answer.append(first_half[i])
        answer.append(second_half[i])
    return answer


print(shuffle_array(nums = [2,5,1,3,4,7], n = 3))