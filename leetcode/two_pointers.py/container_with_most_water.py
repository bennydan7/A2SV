def max_area(height):
    n = len(height)

    max_water = 0
    left = 0
    right = n - 1

    while left < right:
        width = right - left
        h = min(height[left],height[right])
        area = width * h

        max_water = max(max_water,area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
    
print(max_area(height=[1,8,6,2,5,4,8,3,7]))
print(max_area(height=[1,1]))