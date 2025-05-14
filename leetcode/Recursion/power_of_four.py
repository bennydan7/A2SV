def power_of_four(n):
    if n == 1:
        return True
    elif n % 4 != 0 or n < 1:
        return False
    else:
        return power_of_four(n // 4)

print(power_of_four(4))