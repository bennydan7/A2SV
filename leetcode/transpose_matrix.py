def transpose_matrix(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(cols):
        for j in range(rows):
            transpose[i][j] = matrix[j][i]
    return transpose
   


print(transpose_matrix( matrix= [[1,2,3],[4,5,6],[7,8,9]]))
print(transpose_matrix( matrix = [[1,2,3],[4,5,6]]))