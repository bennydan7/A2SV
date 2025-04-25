def equalSubstring(s,t,maxCost):
    n = len(s)
    max_length = 0
    left = 0
    right = 0
    cost = 0
    
    for right in range(n):
        cost += abs(ord(s[right])- ord(t[right]))
    
        while cost > maxCost:
            cost -= abs(ord(s[left])- ord(t[left]))
            left += 1
        max_length = max(max_length,right - left + 1)

    return max_length
        

print(equalSubstring(s = "abcd", t = "bcdf", maxCost = 3))
print(equalSubstring( s = "abcd", t = "cdef", maxCost = 3))
print(equalSubstring(s = "abcd", t = "acde", maxCost = 0))