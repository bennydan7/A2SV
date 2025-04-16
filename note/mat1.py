def findDiagonalOrder(mat):
    rows = len(mat)
    cols = len(mat[0])
    result = []
    row = 0
    col = 0
    is_up = True

    while len(result) < rows * cols:
        result.append(mat[row][col])

        if is_up:
            # Moving up-right
            if col == cols - 1:
                row += 1
                is_up = False
            elif row == 0:
                col += 1
                is_up = False
            else:
                row -= 1
                col += 1
        else:
            # Moving down-left
            if row == rows - 1:
                col += 1
                is_up = True
            elif col == 0:
                row += 1
                is_up = True
            else:
                row += 1
                col -= 1

    return result