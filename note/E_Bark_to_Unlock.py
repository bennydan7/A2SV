def can_unlock(password, n, words):
   
    if password in words:
        return "YES"
    
    for word1 in words:
        for word2 in words:
            if word1[1] == password[0] and word2[0] == password[1]:
                return "YES"
    
    return "NO"

# Read input
password = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# Determine if the phone can be unlocked
result = can_unlock(password, n, words)
print(result)