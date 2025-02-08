
def helpful_maths(s):
    numbers = list(map(int, s.split('+')))
    numbers.sort()
    return '+'.join(map(str, numbers))


s = input().strip()
result = helpful_maths(s)
print(result)