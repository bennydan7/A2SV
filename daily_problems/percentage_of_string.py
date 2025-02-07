# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.


import math

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        length_of_string = len(s)
        characters_in_string= s.count(letter)
        percentage  = math.floor((characters_in_string / length_of_string * 100))
        return percentage
        

    print(percentageLetter("sgawtb","s"))