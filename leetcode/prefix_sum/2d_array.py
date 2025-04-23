def two_D_prefix_sum(matrix):
    row = len(matrix)
    column = len(matrix[0])
    prefix_matrix = [[0] * (column + 1) for _ in range(row + 1)]
    
    for i in range(1,row+1):
        for j in range(1,column+1):
            prefix_matrix[i][j] = matrix[i-1][j-1] + prefix_matrix[i-1][j] + prefix_matrix[i][j-1] - prefix_matrix[i-1][j-1]
    for i in range(1, row + 1):
        print(prefix_matrix[i][1:])

two_D_prefix_sum(matrix = [[3,2,1,4],[6,7,11,9],[0,12,8,15],[3,-1,20,-2]])