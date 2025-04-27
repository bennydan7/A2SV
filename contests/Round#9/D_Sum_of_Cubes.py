t = int(input())
for _ in range(t):
    x = int(input())

    a = 1
    found = False
    while a ** 3 <= x:
        rem = x - a ** 3
        if rem > 0:
            b = round(rem ** (1/3))
            if b ** 3 == rem:
                found = True
                break
        a += 1

    if found: 
        print("YES")
    else:
        print("NO")    
    