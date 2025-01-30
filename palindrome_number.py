class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the integer to a string
        str_x = str(x)
        
        # Check if the string is the same as its reverse
        if str_x == str_x[::-1]:
            return True
        else:
            return False
