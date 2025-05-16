def grid_game(grid):
    col = len(grid[0])
    suffix_sum = [0] + [0] * col + [0]
    prefix_sum = [0] + [0] * col + [0]

    suffix_sum[col] = grid[0][col - 1]
    for i in range(col - 1, 0, -1):
        suffix_sum[i] = suffix_sum[i + 1] + grid[0][i - 1]

    prefix_sum[1] = grid[1][0]
    for i in range(2, col + 1):
        prefix_sum[i] = prefix_sum[i - 1] + grid[1][i - 1]

    output = []
    for i in range(1, col + 1):
        a = suffix_sum[i + 1]
        b = prefix_sum[i - 1]
        max_num = max(a, b)
        output.append(max_num)
    return min(output)

print(grid_game(grid = [[2,5,4],[1,5,1]]))
print(grid_game(grid = [[3,3,1],[8,5,2]]))
print(grid_game( grid = [[1,3,1,15],[1,3,3,1]]))