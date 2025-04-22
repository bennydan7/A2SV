q = int(input())

for _ in range(q):
    a, b, c = map(int, input().split())
    min_distance = float('inf')  

    for move_a in [-1, 0, 1]:
        for move_b in [-1, 0, 1]:
            for move_c in [-1, 0, 1]:
                a_prime = a + move_a
                b_prime = b + move_b
                c_prime = c + move_c
                
                total = abs(a_prime - b_prime) + abs(a_prime - c_prime) + abs(b_prime - c_prime)
                min_distance = min(min_distance, total)

    print(min_distance)
