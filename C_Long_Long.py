t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    max_sum = sum(abs(x) for x in a)
    operations = 0
    in_negative_block = False

    for num in a:
        if num < 0:
            if not in_negative_block:
                operations += 1
                in_negative_block = True
        elif num == 0:
            continue
        else:
            in_negative_block = False

    print(max_sum,operations)
