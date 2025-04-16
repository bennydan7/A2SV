from collections import Counter

def findAnagrams(s,p):
    n = len(s)
    target = Counter(p)
    window_size = len(p)
    counter_s = Counter(s[:window_size])
    results = []
    
    if counter_s == target:
        results.append(0)
    
    for right in range(window_size,n):
        left = right - window_size
        counter_s[s[left]] -= 1
        counter_s[s[right]] += 1

        if counter_s == target:
            results.append(left + 1)
            
    return results

    
print(findAnagrams(s = "abab", p = "ab"))
print(findAnagrams(s = "cbaebabacd", p = "abc"))