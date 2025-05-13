def number_of_nice_subbarray(nums,k):
    res = 0
    odd = 0
    l,m = 0, 0 

    for r in range(len(nums)):
        if nums[r] % 2:
            odd += 1

        while odd > k:
            if nums[l] % 2 :
                odd -= 1
            l += 1
            m = 1

        if odd == k:
            while not nums[m] % 2:
                m += 1
            res += (m - l) + 1
    return res




