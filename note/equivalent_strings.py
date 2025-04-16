
def equivalent_strings(word1,word2):
    if "".join(word1) == "".join(word2):
        return True
    else:
        return False

print(equivalent_strings(word1  = ["abcdd","efg"], word2 = ["abcddefg"]))