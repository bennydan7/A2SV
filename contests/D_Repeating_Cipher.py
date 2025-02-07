def decrypt_repeating_cipher(n, t):
    s = []
    index = 0
    for i in range(1, n + 1):
        if index < n:
            s.append(t[index])
            index += i
        else:
            break
    return ''.join(s)


n = int(input())
t = input()


result = decrypt_repeating_cipher(n, t)
print(result)

