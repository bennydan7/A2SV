from collections import Counter
def permuation_in_string(s1,s2):
        n = len(s2)
        window_size = len(s1)
        if window_size > n:
            return False
        counter_s = Counter(s2[:window_size])
        counter_s1 = Counter(s1)

        if counter_s == counter_s1:
            return True
    
        for right in range(window_size,n):
            left = right - window_size
            counter_s[s2[left]] -= 1
            counter_s[s2[right]] += 1
            if counter_s == counter_s1:
                return True
        return False
        
print(permuation_in_string(s1 = "ab", s2 = "eidbaooo"))
print(permuation_in_string(s1 = "ab", s2 = "eidboaoo"))