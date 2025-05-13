def next_greater_element(nums1,nums2):
    nums1_index = {n:i for i, n in enumerate(nums1)}
    stack = []
    res = [-1] * len(nums2)

    for i in range(len(nums2)):
        cur = nums2[i]
        while stack and cur > stack[-1]:
            val = stack.pop()
            index = nums1_index[val] 
            res[index] = cur
            if cur in nums1:
                stack.append(cur)
    return res
