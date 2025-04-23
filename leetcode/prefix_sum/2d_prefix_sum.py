def d2_prefix_sum(matrix):
    row = len(matrix)
    column = len(matrix[0])
    prefix__sum_array = [[0] * column for _ in range(row)]
    

    for i in range(row):
        for j in range(column):
            prefix__sum_array[i][j] = matrix[i][j]
            if i > 0:
                prefix__sum_array[i][j] += prefix__sum_array[i - 1][j]
            if j > 0:
                prefix__sum_array[i][j] += prefix__sum_array[i][j - 1]
            if i > 0 and j > 0:
                prefix__sum_array[i][j] -= prefix__sum_array[i - 1][j - 1]
    print(prefix__sum_array)
    


d2_prefix_sum(matrix = [[3,2,1,4],[6,7,11,9],[0,12,8,15],[3,-1,20,-2]])