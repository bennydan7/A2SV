def find_diagonal_order(mat):
    rows = len(mat)
    cols = len(mat[0])
    result = []
    row = 0
    col = 0
    is_up = True
    print(cols,rows)

    while len(result) < rows * cols:
        result.append(mat[row][col])

        if is_up:
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



print(find_diagonal_order(mat = [[1,2,3],[4,5,6],[7,8,9]]))