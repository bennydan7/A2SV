from collections import Counter

def longest_substring(s):
    n = len(s)
    left = 0
    counter_s = Counter(s[:left])
    longest = 0

    right = 0
    for left in range(n):
        while right < n and counter_s[s[right]] == 0:
            counter_s[s[right]] += 1
            print(f"in while loop {counter_s}")
            right += 1
        longest = max(longest, right - left)
        counter_s[s[left]] -= 1
        print(counter_s)


print(longest_substring(s = "abcabcbb"))