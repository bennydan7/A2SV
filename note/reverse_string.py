def reverse_string(s):
    reversed = s[::-1]
    return reversed

print(reverse_string(s = ["h","e","l","l","o"]))

def rev_string(s):
    left,right = 0, len(s)- 1
    while left < right:
        s[left],s[right] = s[right],s[left]
        left +=1
        right -=1


print(rev_string(s = ["h","e","l","l","o"]))