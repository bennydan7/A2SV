def magic_squares_in_grid(grid):
    row = len(grid)
    column = len(grid[0])

    def magic(row, cols):
        # Ensure 1 - 9
        values = set()
        for i in range(row,row + 3):
            for j in range(cols, cols  + 3):
                if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                    return 0
                values.add(grid[i][j])
        
        # Rows
        for i in range(r, r + 3):
            if sum(grid[i][c:c+3]) !=  15:
                return 0
            
        # COLS
        for i in range(c, c + 3):
            if (grid[r][i] + grid[r+1][i] + grid[r+2][i]) != 15:
                return 0
            
        # Diagonals
        if (
            grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
            grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15
        ):
            return 0
        return 1
 
    res = 0

    for r in range(row - 2):
        for c in range(column - 2):
            res += magic(r,c)
    return res


print(magic_squares_in_grid(grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
print(magic_squares_in_grid(grid = [[8]]))