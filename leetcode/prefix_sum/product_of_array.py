def product_except_itself(nums):
    answer = []
    n = len(nums)

    total_product = 1
    zero_count = 0


    for num in nums:
        if num != 0:
            total_product *= num
        else:
            zero_count += 1

    for num in nums:
        if zero_count > 1:
            answer.append(0)  
        elif zero_count == 1:
            answer.append(0 if num != 0 else total_product)  
        else:
            answer.append(total_product // num) 
    return answer

print(product_except_itself(nums=[1,2,3,4]))
print(product_except_itself(nums = [-1,1,0,-3,3]))