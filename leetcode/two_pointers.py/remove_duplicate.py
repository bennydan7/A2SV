def remove_duplicates(nums):
    non_duplicates = set(nums)
    non_duplicates_arr = list(non_duplicates)
    print(non_duplicates_arr)
    return len(non_duplicates_arr)



print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))