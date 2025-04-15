def rotate_arrays(nums,k):
    n = len(nums)
    k %= n

    count = 0
    start = 0

    while count < n:
        current = start
        prev = nums[start]

        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev , nums[next_idx]
            current = next_idx
            count += 1
        
            if start == current:
                break

        start +=1

    print(nums)



print(rotate_arrays(nums = [1,2,3,4,5,6,7], k = 3))
print(rotate_arrays(nums = [-1,-100,3,99], k = 2))