def is_greater(a,b):
    return a + b > b + a


def largest_number(nums):
    nums = list(map(str,nums))

    n = len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if not is_greater(nums[j],nums[j + 1]):
                nums[j],nums[j+1] = nums[j + 1] , nums[j]
    
    return f'"{"".join(nums)}"'





        

# print(largest_number(nums = [3,30,34,5,9]))
