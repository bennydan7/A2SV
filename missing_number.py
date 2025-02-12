def missing_num(arr):
    n = len(arr) 
    expected_sum = n * (n + 1) // 2 
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example usage:
print(missing_num([9,6,4,2,3,5,7,0,1]))
