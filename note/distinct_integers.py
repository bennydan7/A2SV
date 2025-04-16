def distinct_integers_after_reverse(nums):
    reversed_integers = []
    for i in nums:
        reversed_integers.append(int(str(i)[::-1]))
    nums.extend(reversed_integers)
    distinct_integers = set(nums)
    return len(distinct_integers)





print(distinct_integers_after_reverse(nums = [1,13,10,12,31]))