def set_matrix_zero(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(i)
        
        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0 
        
        for col in zero_cols:
            for i in range(rows):
                matrix[i][cols] = 0

    return matrix                
print(set_matrix_zero(matrix=[[1,1,1],[1,0,1],[1,1,1]]))