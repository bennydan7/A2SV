def d_repeating_cipher(n,t):
    s = []
    index = 0
    for i in range(1, n+1):
        if index < n:
            s.append(t[index])
            index += i
            print(s)
        else: 
            break
    return "".join(s)

d_repeating_cipher(6,"baabbb")