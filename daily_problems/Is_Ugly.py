def is_ugly(n):
    if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
            return True
    else: return False
       
print(is_ugly(10))