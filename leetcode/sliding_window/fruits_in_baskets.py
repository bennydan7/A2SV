from collections import Counter

def total_fruits(fruits):
    n = len(fruits)
    left = 0
    window = Counter()
    longest = 0

    for right in range(n):
        window[fruits[right]] += 1
        while len(window) > 2:
            window[fruits[left]] -= 1
            if window[fruits[left]] == 0:
                del window[fruits[left]]
            left += 1

        longest = max(longest, right - left + 1)

    return longest


print(total_fruits([1, 2, 1]))  
print(total_fruits([1, 2, 3, 2, 2]))  