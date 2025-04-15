from math import sqrt


def sum_of_squares(c):
    a = 0
    b = int(sqrt(c))
    
    while a <= b:
        sum_squares = a * a + b * b
        if  sum_squares == c :
            return True
        elif sum_squares < c:
            a += 1
        elif sum_squares > c:
            b -= 1
    return False

print(sum_of_squares(c=16))