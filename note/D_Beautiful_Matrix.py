def beautiful_matrix():
    for i in range(1, 5):
        row = list(map(int, input().split()))
        if 1 in row:
            r = i
            c = row.index(1) + 1
            break

    moves = abs(3 - r) + abs(3 - c)
    print(moves)
    

beautiful_matrix()
