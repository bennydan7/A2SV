def shiftingLetters(s, shifts):
    s = list(s)
    diff_array  = [0] * len(s)

    for start,end,direction in shifts:
        if direction == 1:
            diff_array[start] += 1
            if end + 1 < len(diff_array):
                diff_array[end + 1] -= 1
        else:
            diff_array[start] -= 1
            if end + 1 < len(diff_array):
                diff_array[end + 1] += 1

    prefix_sum_array = [0] * len(diff_array)
    prefix_sum_array[0] = diff_array[0]
    for i in range(1,len(diff_array)):
        prefix_sum_array[i] = prefix_sum_array[i - 1] + diff_array[i]
    
    for i in range(len(s)):
        shift = prefix_sum_array[i]
        if shift > 0:
            s[i] = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
        else:
            s[i] = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
    return "".join(s)

print(shiftingLetters(s = "a", shifts = [[0,0,0]]))
print(shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]))
print(shiftingLetters( s = "dztz", shifts = [[0,0,0],[1,1,1]]))