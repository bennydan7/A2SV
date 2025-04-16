grid = [[1,2,4],[3,3,1]]
print(len(grid))

def deleteGreatestValue(grid):

    answer = 0
    while grid[0]:
        max_values = [max(row) for row in grid]
        answer += max(max_values)
        for i in range(len(grid)):
            grid[i].remove(max_values[i])
    return answer