n = int(input())
for i in range(n + 1):
    print(" " * (n - i) + " ".join(map(str, list(range(i)) + list(range(i, -1, -1)))))
for i in range(n - 1, -1, -1):
    print(" " * (n - i) + " ".join(map(str, list(range(i)) + list(range(i, -1, -1)))))