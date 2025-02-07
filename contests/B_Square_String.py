def is_square_string(s):
    n = len(s)
    if n % 2 != 0:
        return "NO"
    mid = n // 2
    if s[:mid] == s[mid:]:
        return "YES"
    return "NO"

def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input().strip()
        results.append(is_square_string(s))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()